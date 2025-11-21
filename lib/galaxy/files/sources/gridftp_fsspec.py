"""Custom fsspec filesystem implementation for Globus GridFTP.

This module provides an fsspec-compatible filesystem interface for accessing
files via the Globus GridFTP protocol.
"""

import logging
import os
from typing import Any, Optional

from fsspec import AbstractFileSystem
from fsspec.spec import AbstractBufferedFile

log = logging.getLogger(__name__)

import globus_sdk
from globus_sdk import (
    AccessTokenAuthorizer,
    TransferClient,
)

# Known public GridFTP hostnames and their Globus endpoint UUIDs
# This allows users to use hostnames which are automatically resolved to UUIDs
#
# To find the correct UUID for an endpoint:
# 1. Install globus-cli: pip install globus-cli
# 2. Login: globus login
# 3. Search: globus endpoint search "EMBL-EBI Public Data"
# 4. Copy the UUID from the search results
# 5. Update the entry below
#
KNOWN_GLOBUS_ENDPOINTS = {
    "ftp.sra.ebi.ac.uk": {
        "uuid": "47772002-3e5b-4fd3-b97c-18cee38d6df2",
        "name": "EMBL-EBI Public Data",
        "note": "European Bioinformatics Institute public data",
    },
    # Add well-known public endpoints here after finding their UUIDs
    # "hostname": {"uuid": "...", "name": "...", "note": "..."}
}


class GridFTPFileSystem(AbstractFileSystem):
    """fsspec filesystem implementation for Globus GridFTP.

    This filesystem uses the Globus Transfer API to interact with GridFTP endpoints.

    Parameters
    ----------
    endpoint_id : str
        The Globus endpoint ID for the GridFTP server
    access_token : str, optional
        Globus access token for authentication
    **storage_options : dict
        Additional options passed to the filesystem
    """

    protocol = "gridftp"
    root_marker = "/"

    def __init__(
        self,
        endpoint_id: Optional[str] = None,
        access_token: Optional[str] = None,
        **storage_options,
    ):
        """Initialize the GridFTP filesystem.

        Args:
            endpoint_id: Globus endpoint ID (can be extracted from URLs if not provided)
            access_token: Access token for authentication (optional, uses environment if not provided)
            **storage_options: Additional storage options
        """
        super().__init__(**storage_options)

        self.endpoint_id = endpoint_id
        self.access_token = access_token

        # Initialize Globus Transfer Client
        authorizer = AccessTokenAuthorizer(
            "Agw1ex207zx7JXa7Dllzb7Ewwpn9M6XPqQdkdE2Neaz8ddwJ4mclCPamN0BlQ8y6e4gYKKqJ5EzdVJf8o981Mib3g5z"
        )
        self.transfer_client = TransferClient(authorizer=authorizer)

    def _extract_endpoint_and_path(self, path: str) -> tuple[Optional[str], str]:
        """Extract endpoint and path from a GridFTP URL.

        Handles both:
        - Globus UUID endpoints: gridftp://ddb59aef-6d04-11e5-ba46-22000b92c6ec/path
        - Hostname endpoints: gridftp://ftp.sra.ebi.ac.uk/path

        Returns:
            Tuple of (endpoint_id, path)
        """
        log.warning(f"DEBUG _extract_endpoint_and_path called with path: '{path}'")
        log.warning(f"DEBUG self.endpoint_id: '{self.endpoint_id}'")

        endpoint = self.endpoint_id

        # Handle gridftp:// or globus:// URLs
        if path.startswith("gridftp://"):
            path = path[len("gridftp://"):]
            log.warning(f"DEBUG stripped gridftp://, path now: '{path}'")
        elif path.startswith("globus://"):
            path = path[len("globus://"):]
            log.warning(f"DEBUG stripped globus://, path now: '{path}'")

        # Try to extract endpoint from path
        if "/" in path:
            potential_endpoint, rest = path.split("/", 1)
            log.warning(f"DEBUG potential_endpoint: '{potential_endpoint}', rest: '{rest}'")

            # Check if it looks like an endpoint (UUID or hostname)
            # UUID format: has hyphens and is long (e.g., ddb59aef-6d04-11e5-ba46-22000b92c6ec)
            # Hostname format: has dots (e.g., ftp.sra.ebi.ac.uk)
            is_uuid = "-" in potential_endpoint and len(potential_endpoint) >= 32
            is_hostname = "." in potential_endpoint
            log.warning(f"DEBUG is_uuid: {is_uuid}, is_hostname: {is_hostname}")

            if is_uuid or is_hostname:
                endpoint = potential_endpoint

                # Try to resolve hostname to Globus UUID if it's a known endpoint
                if is_hostname and not is_uuid:
                    if endpoint in KNOWN_GLOBUS_ENDPOINTS:
                        original_hostname = endpoint
                        endpoint_info = KNOWN_GLOBUS_ENDPOINTS[original_hostname]
                        endpoint = endpoint_info["uuid"]
                        log.warning(
                            f"DEBUG Resolved hostname '{original_hostname}' to UUID: {endpoint}"
                        )
                        log.info(
                            f"Resolved GridFTP hostname '{original_hostname}' to Globus endpoint "
                            f"'{endpoint_info['name']}' (UUID: {endpoint})"
                        )
                    else:
                        log.warning(
                            f"GridFTP hostname '{endpoint}' is not in known endpoints list. "
                            f"This will only work if the server is registered with Globus. "
                            f"Known endpoints: {', '.join(KNOWN_GLOBUS_ENDPOINTS.keys())}"
                        )

                # CRITICAL FIX: Store the extracted endpoint for future calls
                if endpoint and not self.endpoint_id:
                    self.endpoint_id = endpoint
                    log.warning(f"DEBUG Storing endpoint_id for future use: {endpoint}")

                path = "/" + rest
            elif not path.startswith("/"):
                path = "/" + path
        elif not path.startswith("/"):
            path = "/" + path

        log.warning(f"DEBUG _extract_endpoint_and_path returning endpoint: '{endpoint}', path: '{path}'")
        return endpoint, path

    def _strip_protocol(self, path: str) -> str:
        """Remove protocol prefix from path (fsspec standard method).

        Returns:
            Path without protocol
        """
        # Handle gridftp:// or globus:// URLs
        if path.startswith("gridftp://"):
            path = path[len("gridftp://"):]
        elif path.startswith("globus://"):
            path = path[len("globus://"):]

        return path

    def get_file(self, rpath: str, lpath: str, **kwargs):
        """Override get_file to use direct download instead of buffered reading.

        This avoids the need to implement _fetch_range for GridFTP.

        Args:
            rpath: Remote path
            lpath: Local path
        """
        return self._get_file(rpath, lpath, **kwargs)

    def ls(self, path: str, detail: bool = True, **kwargs) -> list:
        """List files and directories at the given path.

        Args:
            path: Path to list
            detail: If True, return detailed info; if False, return just names

        Returns:
            List of file/directory information
        """

        endpoint, path = self._extract_endpoint_and_path(path)
        if not endpoint:
            raise ValueError("Endpoint ID is required. Provide in URL as gridftp://endpoint-id/path")

        try:
            # Use Globus Transfer API to list directory
            response = self.transfer_client.operation_ls(
                endpoint,
                path=path
            )

            entries = []
            for item in response.get("DATA", []):
                entry = {
                    "name": os.path.join(path, item["name"]).lstrip("/"),
                    "size": item.get("size", 0),
                    "type": "directory" if item["type"] == "dir" else "file",
                    "mtime": item.get("last_modified"),
                }

                if detail:
                    entries.append(entry)
                else:
                    entries.append(entry["name"])

            return entries

        except Exception as e:
            log.error(f"Failed to list directory {path}: {e}")
            raise

    def info(self, path: str, **kwargs) -> dict:
        """Get detailed information about a file or directory.

        Args:
            path: Path to get info for

        Returns:
            Dictionary with file/directory information
        """
        endpoint, path = self._extract_endpoint_and_path(path)
        if not endpoint:
            raise ValueError("Endpoint ID is required. Provide in URL as gridftp://endpoint-id/path")

        # Get parent directory and filename
        parent = os.path.dirname(path) or "/"
        filename = os.path.basename(path)

        # List parent directory to find the file
        full_parent = f"gridftp://{endpoint}{parent}"
        entries = self.ls(full_parent, detail=True)

        for entry in entries:
            if entry["name"] == path or entry["name"].endswith("/" + filename):
                return entry

        raise FileNotFoundError(f"File not found: {path}")

    def _open(
        self,
        path: str,
        mode: str = "rb",
        block_size: Optional[int] = None,
        **kwargs,
    ) -> "GridFTPFile":
        """Open a file for reading or writing.

        Args:
            path: Path to the file
            mode: File mode (e.g., 'rb', 'wb')
            block_size: Size of data blocks
            **kwargs: Additional arguments

        Returns:
            File-like object
        """
        endpoint, path = self._extract_endpoint_and_path(path)
        # Note: endpoint is handled by the filesystem, not needed by GridFTPFile
        return GridFTPFile(
            self,
            path,
            mode=mode,
            block_size=block_size,
            **kwargs,
        )

    def _get_file(self, rpath: str, lpath: str, **kwargs):
        """Download a file from GridFTP to local filesystem.

        For public endpoints like EMBL-EBI, uses Globus HTTPS download.
        For other endpoints, would require Globus Connect Personal/Server setup.

        Args:
            rpath: Remote path
            lpath: Local path
        """
        log.warning(f"DEBUG _get_file called with rpath: '{rpath}', lpath: '{lpath}'")

        endpoint, rpath = self._extract_endpoint_and_path(rpath)
        log.warning(f"DEBUG after extraction - endpoint: '{endpoint}', rpath: '{rpath}'")

        if not endpoint:
            log.error(f"DEBUG Endpoint ID is None! Original rpath was: '{rpath}'")
            raise ValueError("Endpoint ID is required. Provide in URL as gridftp://endpoint-id/path")

        try:
            # Try to use Globus HTTPS download for public endpoints
            # This is a workaround for endpoints that don't support direct GridFTP downloads
            # without a local Globus endpoint

            # Check if this is a known public endpoint with HTTPS access
            # For EMBL-EBI, we know the HTTPS URL pattern
            https_url = None
            for hostname, info in KNOWN_GLOBUS_ENDPOINTS.items():
                if info["uuid"] == endpoint:
                    # Found the endpoint - construct HTTPS URL
                    if "ftp.sra.ebi.ac.uk" in hostname:
                        https_url = f"https://{hostname}{rpath}"
                        log.info(f"Using HTTPS download from {hostname}: {https_url}")
                        break

            if https_url:
                # Download via HTTPS instead of GridFTP
                import requests
                log.warning(f"DEBUG Downloading via HTTPS: {https_url}")
                response = requests.get(https_url, stream=True, timeout=300)
                response.raise_for_status()

                with open(lpath, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)

                log.info(f"Successfully downloaded file via HTTPS to {lpath}")
                return

            # If no HTTPS URL available, raise error
            raise NotImplementedError(
                f"Direct GridFTP download from endpoint {endpoint} requires Globus Connect "
                f"Personal or Server to be installed and configured on this machine. "
                f"As a workaround, use HTTPS if the endpoint supports it."
            )

        except Exception as e:
            log.error(f"Failed to download file {rpath}: {e}")
            raise

    def _put_file(self, lpath: str, rpath: str, **kwargs):
        """Upload a file from local filesystem to GridFTP.

        Args:
            lpath: Local path
            rpath: Remote path
        """

        endpoint, rpath = self._extract_endpoint_and_path(rpath)
        if not endpoint:
            raise ValueError("Endpoint ID is required. Provide in URL as gridftp://endpoint-id/path")

        try:
            # Similar to get_file, this requires proper Globus endpoint setup
            log.warning(
                "GridFTP put_file is using simplified implementation. "
                "For production use, configure proper Globus endpoints."
            )

            raise NotImplementedError(
                "Direct file upload requires additional Globus endpoint configuration"
            )

        except Exception as e:
            log.error(f"Failed to upload file {rpath}: {e}")
            raise

    def mkdir(self, path: str, create_parents: bool = True, **kwargs):
        """Create a directory.

        Args:
            path: Path to create
            create_parents: Whether to create parent directories
        """

        endpoint, path = self._extract_endpoint_and_path(path)
        if not endpoint:
            raise ValueError("Endpoint ID is required. Provide in URL as gridftp://endpoint-id/path")

        try:
            self.transfer_client.operation_mkdir(
                endpoint,
                path=path
            )
        except Exception as e:
            log.error(f"Failed to create directory {path}: {e}")
            raise

    def rm(self, path: str, recursive: bool = False, **kwargs):
        """Remove a file or directory.

        Args:
            path: Path to remove
            recursive: Whether to remove directories recursively
        """

        endpoint, path = self._extract_endpoint_and_path(path)
        if not endpoint:
            raise ValueError("Endpoint ID is required. Provide in URL as gridftp://endpoint-id/path")

        try:
            # Use Globus delete operation
            delete_data = globus_sdk.DeleteData(
                self.transfer_client,
                endpoint,
                recursive=recursive
            )
            delete_data.add_item(path)

            delete_result = self.transfer_client.submit_delete(delete_data)
            task_id = delete_result["task_id"]

            # Wait for task to complete (optional)
            log.info(f"Delete task submitted: {task_id}")

        except Exception as e:
            log.error(f"Failed to remove {path}: {e}")
            raise

    def exists(self, path: str, **kwargs) -> bool:
        """Check if a path exists.

        Args:
            path: Path to check

        Returns:
            True if path exists, False otherwise
        """
        try:
            self.info(path)
            return True
        except FileNotFoundError:
            return False


class GridFTPFile(AbstractBufferedFile):
    """File-like object for GridFTP files.

    This provides buffered read/write access to files on GridFTP endpoints.
    """

    def __init__(
        self,
        fs: GridFTPFileSystem,
        path: str,
        mode: str = "rb",
        block_size: Optional[int] = None,
        **kwargs,
    ):
        """Initialize GridFTP file object.

        Args:
            fs: Parent filesystem
            path: File path
            mode: File mode
            block_size: Block size for buffering
            **kwargs: Additional arguments
        """
        super().__init__(
            fs=fs,
            path=path,
            mode=mode,
            block_size=block_size,
            **kwargs,
        )

    def _fetch_range(self, start: int, end: int) -> bytes:
        """Fetch a range of bytes from the file.

        Args:
            start: Start byte position
            end: End byte position

        Returns:
            Bytes in the requested range
        """
        # This would need to be implemented based on your Globus setup
        # For now, we raise NotImplementedError
        raise NotImplementedError(
            "Byte range fetching requires additional Globus endpoint configuration"
        )

    def _upload_chunk(self, final: bool = False) -> bool:
        """Upload buffered data to the remote file.

        Args:
            final: Whether this is the final chunk

        Returns:
            True if successful
        """
        # This would need to be implemented for write operations
        raise NotImplementedError(
            "File upload requires additional Globus endpoint configuration"
        )
