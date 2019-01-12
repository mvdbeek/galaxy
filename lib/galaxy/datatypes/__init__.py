try:
    import routes
    url_for = routes.url_for
except ImportError:
    # Don't need this if just setting metadata
    def url_for(*args):
        return None
