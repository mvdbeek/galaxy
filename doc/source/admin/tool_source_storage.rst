Tool Source Storage
===================

Galaxy can cache parsed tool sources to improve startup time and reduce memory usage
when serving batch API endpoints. This is especially useful for large Galaxy installations
with thousands of tools.

Overview
--------

By default, Galaxy loads all tools into memory at startup. For installations with many tools,
this can:

- Slow down Galaxy startup significantly
- Consume large amounts of memory

The tool source storage system addresses these issues by:

1. Pre-parsing and storing tool sources in a configurable backend
2. Maintaining a lightweight index in memory for fast API responses
3. Loading full Tool objects on-demand with LRU caching

Configuration
-------------

Tool source storage is configured in ``galaxy.yml``. The following options are available:

Backend Selection
^^^^^^^^^^^^^^^^^

.. code-block:: yaml

    galaxy:
      # Backend for storing tool sources: 'database', 'redis', or 'disk'
      tool_source_store: database

**Database Backend** (default)

Stores tool sources in the Galaxy database. Best for:

- Single-server deployments
- Installations where tools don't change frequently
- Simplest setup (no additional infrastructure)

**Redis Backend**

Stores tool sources in Redis. Best for:

- Multi-server deployments where Galaxy processes need to share cache
- High-availability setups

.. code-block:: yaml

    galaxy:
      tool_source_store: redis
      tool_source_redis_url: redis://localhost:6379/1
      # Optional: Set TTL for automatic expiry (in seconds)
      tool_source_redis_ttl: 86400  # 24 hours

For Redis Sentinel:

.. code-block:: yaml

    galaxy:
      tool_source_redis_url: redis+sentinel://sentinel1:26379,sentinel2:26379/mymaster/0

**Disk Backend**

Stores tool sources on the filesystem. Best for:

- Avoiding database load
- Environments with fast local storage (SSD/NVMe)
- Distribution via CVMFS for shared read-only access across clusters

.. code-block:: yaml

    galaxy:
      tool_source_store: disk
      tool_source_disk_path: /path/to/tool_sources  # or relative to data_dir

Cache Configuration
^^^^^^^^^^^^^^^^^^^

.. code-block:: yaml

    galaxy:
      # Maximum Tool objects in LRU cache (default: 500)
      tool_cache_size: 500

      # TTL for pre-computed API responses in seconds (default: 300)
      tool_api_cache_ttl: 300

The ``tool_cache_size`` determines how many fully-loaded Tool objects are kept in memory.
A typical Galaxy installation has 500-2000 tools. If you frequently use many different
tools, increase this value.

The ``tool_api_cache_ttl`` controls how long pre-computed responses for batch endpoints
are cached. Lower values mean more frequent updates but higher CPU usage.

Populating the Tool Source Store
--------------------------------

After configuring tool source storage, you need to populate it with your tools.
Use the ``populate_store.py`` script:

Basic Usage
^^^^^^^^^^^

.. code-block:: console

    $ python scripts/tool_source/populate_store.py

This will:

1. Scan all configured tool directories
2. Parse each tool and extract metadata
3. Store the tool sources in the configured backend
4. Build and store the tool index

Command Line Options
^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    $ python scripts/tool_source/populate_store.py --help

    Options:
      --config, -c PATH      Path to galaxy.yml (default: config/galaxy.yml)
      --tool-conf PATH       Path to tool_conf.xml (can specify multiple times)
      --incremental          Only process new/changed tools
      --rebuild-index        Force rebuild of the tool index
      --dry-run              Show what would be done without making changes
      --verbose, -v          Verbose output

Examples
^^^^^^^^

**Initial population:**

.. code-block:: console

    $ python scripts/tool_source/populate_store.py -c /path/to/galaxy.yml

**Incremental update after adding new tools:**

.. code-block:: console

    $ python scripts/tool_source/populate_store.py --incremental

**Rebuild index without re-parsing tools:**

.. code-block:: console

    $ python scripts/tool_source/populate_store.py --rebuild-index

Automation with Cron
^^^^^^^^^^^^^^^^^^^^

For installations where tools are frequently updated, you can run the population
script on a schedule:

.. code-block:: cron

    # Update tool source store every hour
    0 * * * * /path/to/galaxy/.venv/bin/python /path/to/galaxy/scripts/tool_source/populate_store.py --incremental >> /var/log/galaxy/tool_source_update.log 2>&1

Watch Mode (Live Updates)
^^^^^^^^^^^^^^^^^^^^^^^^^

For development environments or installations where tools change frequently, you can run
the population script in watch mode. This uses ``watchdog`` to monitor tool directories
for changes and automatically updates the store, then sends a notification via Kombu
to trigger cache reloads in all Galaxy processes.

.. code-block:: console

    $ python scripts/tool_source/populate_store.py --config galaxy.yml --watch

Watch mode options:

- ``--watch, -w`` - Enable watch mode
- ``--watch-polling`` - Use polling observer (required for network filesystems like NFS/CVMFS)
- ``--debounce SECS`` - Debounce time for file changes (default: 2.0 seconds)

Example with polling for network filesystem:

.. code-block:: console

    $ python scripts/tool_source/populate_store.py -c galaxy.yml --watch --watch-polling --debounce 5.0

**Requirements:**

- The ``watchdog`` library must be installed: ``pip install watchdog``
- Galaxy must have ``amqp_internal_connection`` configured for Kombu notifications
- All Galaxy processes must be connected to the same AMQP broker

When a tool XML file changes, watch mode will:

1. Detect the file change (with debouncing to handle rapid edits)
2. Re-parse the tool and update the store
3. Send a ``reload_tool_source_cache`` control message via Kombu
4. All Galaxy processes will invalidate their local caches

This is useful for:

- Development environments where tools are being actively edited
- CI/CD pipelines that deploy tool updates
- Installations using shared storage where tools may be updated externally

API Endpoints
-------------

The tool source storage system provides several API endpoints for monitoring and management:

Tool Sources
^^^^^^^^^^^^

- ``GET /api/tool_sources`` - List stored tool sources
- ``GET /api/tool_sources/stats`` - Get storage statistics
- ``GET /api/tool_sources/{hash}`` - Get a specific tool source by hash
- ``GET /api/tool_sources/by_tool/{tool_id}`` - Get tool sources by tool ID

Tool Index
^^^^^^^^^^

- ``GET /api/tool_index`` - List tool index entries
- ``GET /api/tool_index/stats`` - Get index statistics
- ``GET /api/tool_index/{tool_id}`` - Get a specific index entry
- ``GET /api/tool_index/search?q=query`` - Search the tool index

Cache Management
^^^^^^^^^^^^^^^^

- ``GET /api/tool_cache/stats`` - Get cache statistics
- ``POST /api/tool_cache/clear`` - Clear the Tool object cache

Example: Check cache statistics:

.. code-block:: console

    $ curl -H "x-api-key: $GALAXY_API_KEY" https://galaxy.example.org/api/tool_cache/stats

Benchmarking
------------

To benchmark tool source deserialization performance, use the benchmarks module:

.. code-block:: console

    $ python -m galaxy.tool_source_store.benchmarks --tools-dir /path/to/tools -n 100

This will measure:

- Index serialization/deserialization time
- Tool source storage and retrieval time
- XML parsing time
- Memory usage estimates

Troubleshooting
---------------

Tools not appearing in the index
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Verify the tool source store is configured:

   .. code-block:: console

       $ curl https://galaxy.example.org/api/tool_sources/stats

2. Re-run the population script with verbose output:

   .. code-block:: console

       $ python scripts/tool_source/populate_store.py -v

3. Check for parsing errors in the Galaxy log

High memory usage
^^^^^^^^^^^^^^^^^

1. Reduce ``tool_cache_size`` to cache fewer Tool objects
2. Ensure the tool index is being used (check ``/api/tool_index/stats``)
3. Consider using the disk backend to reduce database memory pressure

Slow batch endpoints
^^^^^^^^^^^^^^^^^^^^

1. Verify the tool index is populated: ``GET /api/tool_index/stats``
2. Check that ``tool_api_cache_ttl`` is not set to 0
3. Ensure the lazy toolbox is being used by checking cache stats

Redis connection issues
^^^^^^^^^^^^^^^^^^^^^^^

1. Verify Redis is running and accessible
2. Check the Redis URL format
3. For Sentinel setups, verify all sentinel hosts are reachable
4. Check Redis memory limits and eviction policies

Migration from Traditional Toolbox
----------------------------------

To migrate an existing Galaxy installation to use tool source storage:

1. Add the configuration to ``galaxy.yml``:

   .. code-block:: yaml

       galaxy:
         tool_source_store: database  # or redis/disk

2. Run the population script:

   .. code-block:: console

       $ python scripts/tool_source/populate_store.py

3. Restart Galaxy

4. Verify the migration:

   .. code-block:: console

       $ curl https://galaxy.example.org/api/tool_index/stats
       $ curl https://galaxy.example.org/api/tool_cache/stats

The traditional toolbox will continue to work as a fallback if the tool source
store is not populated or if a specific tool is not found in the store.
