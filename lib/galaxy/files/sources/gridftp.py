"""Galaxy file source plugin for Globus GridFTP.

This plugin allows Galaxy to access files stored on Globus GridFTP endpoints
using the fsspec interface.
"""

import logging
from typing import (
    Optional,
    Union,
)

from galaxy.files.models import FilesSourceRuntimeContext
from galaxy.files.sources import PluginKind
from galaxy.files.sources._fsspec import (
    CacheOptionsDictType,
    FsspecBaseFileSourceConfiguration,
    FsspecBaseFileSourceTemplateConfiguration,
    FsspecFilesSource,
)
from galaxy.util.config_templates import TemplateExpansion

try:
    from .gridftp_fsspec import GridFTPFileSystem
except ImportError:
    GridFTPFileSystem = None


REQUIRED_PACKAGE = "globus-sdk"
FS_PLUGIN_TYPE = "gridftp"

log = logging.getLogger(__name__)


class GridFTPFileSourceTemplateConfiguration(FsspecBaseFileSourceTemplateConfiguration):
    """Template configuration for GridFTP file source.

    This configuration is used to define the template that can be expanded
    with user-specific values.
    """

    endpoint_id: Union[str, TemplateExpansion, None] = None
    """Globus endpoint ID for the GridFTP server. Can be extracted from URLs if not provided."""

    access_token: Union[str, TemplateExpansion, None] = None
    """Globus access token for authentication. Can be provided via template expansion or from environment."""

    path: Union[str, TemplateExpansion, None] = None
    """Base path within the endpoint (optional)."""


class GridFTPFileSourceConfiguration(FsspecBaseFileSourceConfiguration):
    """Resolved configuration for GridFTP file source.

    This is the configuration after template expansion, with all values resolved.
    """

    endpoint_id: Optional[str] = None
    """Globus endpoint ID for the GridFTP server. Can be extracted from URLs if not provided."""

    access_token: Optional[str] = None
    """Globus access token for authentication."""

    path: Optional[str] = None
    """Base path within the endpoint."""


class GridFTPFilesSource(
    FsspecFilesSource[GridFTPFileSourceTemplateConfiguration, GridFTPFileSourceConfiguration]
):
    """Galaxy file source for Globus GridFTP endpoints.

    This file source plugin enables Galaxy to:
    - Browse files on Globus GridFTP endpoints
    - Download files from GridFTP to Galaxy
    - Upload files from Galaxy to GridFTP
    - Perform basic file operations (list, info, etc.)

    Configuration example:
    ```yaml
    - type: gridftp
      id: my_gridftp
      label: My GridFTP Endpoint
      doc: Access files via Globus GridFTP
      endpoint_id: "your-endpoint-uuid"
      access_token: "{{ user.preferences['globus_access_token'] }}"
    ```
    """

    plugin_type = FS_PLUGIN_TYPE
    plugin_kind = PluginKind.stock
    required_module = GridFTPFileSystem
    required_package = REQUIRED_PACKAGE

    template_config_class = GridFTPFileSourceTemplateConfiguration
    resolved_config_class = GridFTPFileSourceConfiguration

    def __init__(self, template_config: GridFTPFileSourceTemplateConfiguration):
        """Initialize the GridFTP file source with default values."""
        defaults = dict(
            id="_gridftp",
            label="Globus GridFTP",
            doc="Access files via Globus GridFTP protocol",
            writable=False,
            browsable=False,  # Not browsable without endpoint ID
        )
        template_config = self._apply_defaults_to_template(defaults, template_config)
        super().__init__(template_config)

    def _open_fs(
        self,
        context: FilesSourceRuntimeContext[GridFTPFileSourceConfiguration],
        cache_options: CacheOptionsDictType,
    ) -> GridFTPFileSystem:
        """Open a GridFTP filesystem instance.

        Args:
            context: Runtime context with resolved configuration
            cache_options: Cache options for the filesystem

        Returns:
            Initialized GridFTPFileSystem instance

        Raises:
            Exception: If the required package is not installed
        """
        if GridFTPFileSystem is None:
            raise self.required_package_exception

        config = context.config

        # Initialize the GridFTP filesystem
        fs = GridFTPFileSystem(
            endpoint_id=config.endpoint_id,
            access_token=config.access_token,
            **cache_options,
        )

        return fs

    def _to_endpoint_path(self, path: str, config: GridFTPFileSourceConfiguration) -> str:
        """Convert a path to the full endpoint path.

        If a base path is configured, prepend it to the given path.

        Args:
            path: Path relative to the file source
            config: Resolved configuration

        Returns:
            Full path on the endpoint
        """
        if config.path:
            # Normalize paths
            base_path = config.path.rstrip("/")
            path = path.lstrip("/")
            return f"{base_path}/{path}" if path else base_path

        return path

    def _adapt_entry_path(self, filesystem_path: str) -> str:
        """Remove the base path from filesystem paths for display.

        Args:
            filesystem_path: Full path on the filesystem

        Returns:
            Path relative to the file source root
        """
        if self.template_config.path:
            base_path = str(self.template_config.path).rstrip("/")
            if filesystem_path.startswith(base_path):
                relative_path = filesystem_path[len(base_path):]
                return relative_path.lstrip("/") if relative_path else "/"

        return filesystem_path

    def _to_filesystem_path(self, path: str) -> str:
        """Convert entry path to filesystem path.

        Args:
            path: Path from the API

        Returns:
            Path for the filesystem
        """
        # Get the runtime context from the current request
        # Note: This is a simplified version - in practice, you'd get the config
        # from the context parameter in list/realize methods
        if hasattr(self, "_current_config") and self._current_config.path:
            return self._to_endpoint_path(path, self._current_config)

        return path

    def _list(
        self,
        context: FilesSourceRuntimeContext[GridFTPFileSourceConfiguration],
        path="/",
        recursive=False,
        write_intent: bool = False,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        query: Optional[str] = None,
        sort_by: Optional[str] = None,
    ):
        """List files and directories.

        Args:
            context: Runtime context
            path: Path to list
            recursive: Whether to list recursively
            write_intent: Whether listing is for write operation
            limit: Maximum number of entries to return
            offset: Offset for pagination
            query: Search query
            sort_by: Sort field

        Returns:
            Tuple of (entries, total_count)
        """
        # Store config for path conversion
        self._current_config = context.config

        # Convert path to endpoint path
        endpoint_path = self._to_endpoint_path(path, context.config)

        # Call parent implementation with converted path
        return super()._list(
            context=context,
            path=endpoint_path,
            recursive=recursive,
            write_intent=write_intent,
            limit=limit,
            offset=offset,
            query=query,
            sort_by=sort_by,
        )

    def _realize_to(
        self,
        source_path: str,
        native_path: str,
        context: FilesSourceRuntimeContext[GridFTPFileSourceConfiguration],
    ):
        """Download a file from GridFTP to local filesystem.

        Args:
            source_path: Path on GridFTP endpoint
            native_path: Local path to download to
            context: Runtime context
        """
        # For stock plugin with no configured endpoint, ensure path includes endpoint
        # Format expected by fsspec: gridftp://endpoint/path or just endpoint/path
        if not context.config.endpoint_id and not source_path.startswith("gridftp://"):
            # Path might be like "ftp.sra.ebi.ac.uk/vol1/..." or just "/vol1/..."
            # We need it in a format the fsspec can extract endpoint from
            if not ("/" in source_path and "." in source_path.split("/")[0]):
                # Just a path like "/vol1/...", can't extract endpoint
                log.warning(f"Cannot extract endpoint from path: {source_path}")
            # If it has endpoint/path format, prepend protocol
            if not source_path.startswith("/"):
                source_path = f"gridftp://{source_path}"

        endpoint_path = self._to_endpoint_path(source_path, context.config)
        super()._realize_to(source_path=endpoint_path, native_path=native_path, context=context)

    def _write_from(
        self,
        target_path: str,
        native_path: str,
        context: FilesSourceRuntimeContext[GridFTPFileSourceConfiguration],
    ):
        """Upload a file from local filesystem to GridFTP.

        Args:
            target_path: Path on GridFTP endpoint
            native_path: Local path to upload from
            context: Runtime context
        """
        endpoint_path = self._to_endpoint_path(target_path, context.config)
        super()._write_from(target_path=endpoint_path, native_path=native_path, context=context)

    def score_url_match(self, url: str) -> int:
        """Score how well this file source matches a URL.

        Args:
            url: URL to match

        Returns:
            Match score (higher is better, 0 means no match)
        """
        # Match gridftp:// URLs
        if url.startswith("gridftp://"):
            # If endpoint is configured, give higher score for matching URLs
            if self.template_config.endpoint_id:
                endpoint_id = str(self.template_config.endpoint_id)
                if endpoint_id in url:
                    return len(f"gridftp://{endpoint_id}")
            # Still match any gridftp:// URL
            return len("gridftp://")

        # Match globus:// URLs (alternative protocol)
        if url.startswith("globus://"):
            if self.template_config.endpoint_id:
                endpoint_id = str(self.template_config.endpoint_id)
                if endpoint_id in url:
                    return len(f"globus://{endpoint_id}")
            return len("globus://")

        return super().score_url_match(url)


__all__ = ("GridFTPFilesSource",)
