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

Toolbox Selection
^^^^^^^^^^^^^^^^^

.. code-block:: yaml

    galaxy:
      # Force the lazy toolbox on/off. When unset (the default), the lazy
      # toolbox is enabled automatically if the tool source store is populated.
      use_lazy_toolbox: null

When ``use_lazy_toolbox`` is left unset, Galaxy auto-detects: if the configured
store contains at least one tool, the LazyToolBox is used; otherwise Galaxy
falls back to the traditional eager ToolBox. Set the value explicitly to
override auto-detection.

Per-conf Store Routing (CVMFS Recipe)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Individual ``tool_conf`` files can opt into a *named* tool source store,
distinct from the global default. The typical use case is shipping a
read-only SQLite bundle on CVMFS alongside a tool_conf, so worker
processes can resolve every tool in that conf with local-cached lookups
instead of one network round-trip per JSON file.

Declare the named stores under the new top-level ``tool_source_stores``
key in ``galaxy.yml``. The ``sqlalchemy`` backend takes either a SQLAlchemy
``url`` or a ``path`` shortcut that builds a SQLite URL. SQLite is the
typical choice for CVMFS bundles (single self-contained file), but any
SQLAlchemy-supported database works:

.. code-block:: yaml

    galaxy:
      tool_source_store: database          # the writable default
      tool_source_stores:
        cvmfs_main:
          backend: sqlalchemy
          path: /cvmfs/example.org/tools/sources.sqlite
          read_only: true
        site_shared:
          backend: sqlalchemy
          url: postgresql://galaxy_ro@db.example.org/tool_sources
          read_only: true

Then point the tool_conf at it via the root element's ``store`` attribute
(XML) or top-level key (YAML):

.. code-block:: xml

    <?xml version="1.0"?>
    <toolbox store="cvmfs_main">
      <section id="cvmfs_tools" name="CVMFS Tools">
        <tool file="bwa/bwa.xml"/>
        ...
      </section>
    </toolbox>

At startup, Galaxy inspects every ``tool_conf`` for the attribute, builds
the referenced stores, and wraps them with the writable default in a
composite store. Reads are tried in declared order (first hit wins) and
writes always go to the default store. If no tool_conf opts in, the
default store is used directly with zero overhead.

**Building the bundle**

Build the SQLite file from a writable host before shipping it:

.. code-block:: console

    $ python scripts/tool_source/populate_store.py -c galaxy.yml --target cvmfs_main

Use ``--target`` to restrict population to a single named store; without
it, ``populate_store.py`` populates **every writable store** referenced
from a tool_conf in the same run.

Once the bundle is in place on CVMFS (or any read-only mount), restart
Galaxy. The composite store reports its members in
``GET /api/tool_sources/stats`` and ``backend`` will be ``composite``.

**Why SQLite for CVMFS?** The disk backend stores one JSON file per tool
hash, so each ``get(hash)`` becomes a separate filesystem operation —
expensive on a network-mounted store. SQLite is a single file with B-tree
indexes; once the page cache is warm, lookups stay local. For shared
deployments without CVMFS, point ``url:`` at any SQLAlchemy-supported
backend (Postgres, MySQL, …) instead.

Cache Configuration
^^^^^^^^^^^^^^^^^^^

.. code-block:: yaml

    galaxy:
      # Maximum Tool objects in the LazyToolBox LRU cache (default: 500)
      lazy_toolbox_cache_size: 500

      # TTL for pre-computed API responses in seconds (default: 300)
      tool_api_cache_ttl: 300

The ``lazy_toolbox_cache_size`` determines how many fully-loaded Tool objects
are kept in memory by the LazyToolBox. A typical Galaxy installation has
500-2000 tools. If you frequently use many different tools, increase this value.

The ``tool_api_cache_ttl`` controls how long pre-computed responses for batch
endpoints (``/api/tools``, ``/api/tools/tests_summary``, ``/api/tool_panels``,
etc.) are cached. Set to ``0`` to disable caching.

Populating the Tool Source Store
--------------------------------

After configuring tool source storage, you need to populate it with your tools.
Use the ``populate_store.py`` script:

Basic Usage
^^^^^^^^^^^

.. code-block:: console

    $ python scripts/tool_source/populate_store.py --config /path/to/galaxy.yml

This will:

1. Discover tools from your tool configs (uses the same logic as Galaxy startup)
2. Parse each tool (with macro expansion) and compute a content hash
3. Store the tool sources in the configured backend (skipping unchanged tools)

Note: ``--config`` is required; the script does not assume a default path.

Command Line Options
^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    $ python scripts/tool_source/populate_store.py --help

    Options:
      --config, -c PATH      Galaxy configuration file (required)
      --dry-run              Show what would be stored without storing
      --incremental          Only store new/changed tools (default)
      --full                 Force re-store of all tools
      --tool-id PATTERN      Only process tools whose ID contains PATTERN
      --parallel, -j N       Number of parallel workers (default: 4)
      --rebuild-index        Rebuild the tool index after population
      --target NAME          Restrict to a single named store from
                             tool_source_stores (or '__default__'). Without
                             this, every writable store is populated.
      --verbose, -v          Verbose output
      --watch, -w            Watch tool directories and send reload notifications
      --watch-polling        Use polling observer (for NFS/CVMFS/network FS)
      --debounce SECS        Debounce time for watch mode (default: 2.0)

Examples
^^^^^^^^

**Initial population:**

.. code-block:: console

    $ python scripts/tool_source/populate_store.py -c /path/to/galaxy.yml

**Force re-store everything (e.g., after a parser change):**

.. code-block:: console

    $ python scripts/tool_source/populate_store.py -c galaxy.yml --full

**Process only a subset of tools:**

.. code-block:: console

    $ python scripts/tool_source/populate_store.py -c galaxy.yml --tool-id samtools

Automation with Cron
^^^^^^^^^^^^^^^^^^^^

For installations where tools are frequently updated, you can run the population
script on a schedule:

.. code-block:: cron

    # Update tool source store every hour (incremental is the default)
    0 * * * * /path/to/galaxy/.venv/bin/python /path/to/galaxy/scripts/tool_source/populate_store.py -c /path/to/galaxy.yml >> /var/log/galaxy/tool_source_update.log 2>&1

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

The tool source storage system provides several API endpoints for monitoring
and management. Endpoints marked **(admin)** require an admin API key.

Tool Sources (all admin-only)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``GET /api/tool_sources`` **(admin)** - List stored tool sources
- ``GET /api/tool_sources/stats`` **(admin)** - Get storage statistics
- ``GET /api/tool_sources/{hash}`` **(admin)** - Get a specific tool source by hash
- ``GET /api/tool_sources/by_tool/{tool_id}`` **(admin)** - Get tool sources by tool ID

Tool Index
^^^^^^^^^^

- ``GET /api/tool_index`` - List tool index entries
- ``GET /api/tool_index/stats`` **(admin)** - Get index statistics
- ``GET /api/tool_index/{tool_id}`` - Get a specific index entry
- ``GET /api/tool_index/search?q=query`` - Search the tool index

Cache Management (all admin-only)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``GET /api/tool_cache/stats`` **(admin)** - Get LazyToolBox cache statistics
- ``POST /api/tool_cache/clear`` **(admin)** - Clear the Tool object LRU cache

Example: Check cache statistics:

.. code-block:: console

    $ curl -H "x-api-key: $GALAXY_API_KEY" https://galaxy.example.org/api/tool_cache/stats

Benchmarking
------------

To benchmark tool source deserialization performance, use the benchmarks module:

.. code-block:: console

    $ PYTHONPATH=lib python -m galaxy.tool_source_store.benchmarks --iterations 100

Performance Results
^^^^^^^^^^^^^^^^^^^

The following benchmarks were run on a typical server (results may vary based on hardware):

**Core Operations (1000 tool index)**

================================  ==========  ==============
Operation                         Mean Time   Throughput
================================  ==========  ==============
XML tool parsing                  0.10 ms     ~10,000/sec
Hash computation                  0.01 ms     ~115,000/sec
Index search (3 queries)          2.5 ms      ~400/sec
API response generation           0.35 ms     ~2,800/sec
All requirements aggregation      0.48 ms     ~2,000/sec
Index serialization               2.1 ms      ~470/sec
Index deserialization             2.3 ms      ~430/sec
================================  ==========  ==============

**Scaling by Index Size**

===========  ===============  ==============  ============
Tool Count   API Response     Index Search    Memory (JSON)
===========  ===============  ==============  ============
100          0.03 ms          0.2 ms          73 KB
500          0.14 ms          1.0 ms          367 KB
1,000        0.38 ms          1.9 ms          735 KB
2,000        0.69 ms          4.2 ms          1.4 MB
5,000        2.9 ms           10.5 ms         3.6 MB
===========  ===============  ==============  ============

**Startup Time Comparison (1000 tools)**

Measured on test system (100 real Galaxy tools, extrapolated to 1000):

- Traditional (parse all XML at startup): ~84 ms
- Index-based (load pre-computed index): ~10 ms
- **Startup speedup: ~8x**

Note: The index must be pre-populated using ``populate_store.py``. The speedup
applies to Galaxy process startup time, not total initial setup time.

The index-based approach provides significant benefits for large installations:

- Faster Galaxy startup time
- Reduced memory usage (only frequently-used tools in cache)
- Quick batch API responses from pre-computed index

Troubleshooting
---------------

Tools not appearing in the index
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Verify the tool source store is configured (admin API key required):

   .. code-block:: console

       $ curl -H "x-api-key: $GALAXY_API_KEY" https://galaxy.example.org/api/tool_sources/stats

2. Re-run the population script with verbose output:

   .. code-block:: console

       $ python scripts/tool_source/populate_store.py -c galaxy.yml -v

3. Check for parsing errors in the Galaxy log

High memory usage
^^^^^^^^^^^^^^^^^

1. Reduce ``lazy_toolbox_cache_size`` to cache fewer Tool objects
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
