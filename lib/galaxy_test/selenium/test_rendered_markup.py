"""Check what the client's DOMPurify profiles keep and drop in a real browser.

The client unit tests replace the sanitizer with a spy because DOMPurify
doesn't run correctly under happy-dom, so these cover the real thing.
"""

from .framework import (
    selenium_test,
    SeleniumTestCase,
)

LIBRARY_DESCRIPTION = (
    "<b>Bold</b> notes at https://galaxyproject.org "
    "<style>body { display: none; }</style>"
    "<form><button>Go</button></form>"
    '<a href="javascript:void(0)">plain link</a>'
    '<img src="missing.png" onerror="window.markupHandlerRan = true">'
)


class TestRenderedMarkup(SeleniumTestCase):
    run_as_admin = True

    def setup_with_driver(self):
        super().setup_with_driver()
        self.admin_login()

    @selenium_test
    def test_library_description_keeps_formatting_and_drops_page_level_markup(self):
        name = self._get_random_name(prefix="markup")
        self.dataset_populator._post("libraries", data={"name": name, "description": LIBRARY_DESCRIPTION}, json=True)

        self.libraries_open()
        self.libraries_index_search_for(name)
        # Long descriptions start out truncated
        self.wait_for_selector_clickable(".more-text-btn").click()
        self.wait_for_selector_visible(".text-field b")

        description = self.execute_script("""
            const field = [...document.querySelectorAll(".text-field")].find((el) => el.querySelector("b"));
            return {
                bold: field.querySelector("b").textContent,
                linkified: field.querySelector("a[href='https://galaxyproject.org']") !== null,
                style: field.querySelector("style") !== null,
                form: field.querySelector("form, button") !== null,
                plainLink: field.querySelector("a:not([href])")?.textContent ?? null,
                imageHandler: field.querySelector("img")?.getAttribute("onerror") ?? null,
                handlerRan: window.markupHandlerRan === true,
            };
            """)
        assert description == {
            "bold": "Bold",
            "linkified": True,
            "style": False,
            "form": False,
            "plainLink": "plain link",
            "imageHandler": None,
            "handlerRan": False,
        }

    @selenium_test
    def test_html_page_links_opening_a_new_window_drop_the_opener(self):
        page = self.dataset_populator.new_page(
            slug=self._get_random_name(prefix="links"),
            content=(
                '<p><a href="https://galaxyproject.org/new-tab" target="_blank">new tab</a> '
                '<a href="https://galaxyproject.org/same-tab" target="_top">same tab</a></p>'
            ),
        )
        self.get(f"published/page?id={page['id']}")
        self.wait_for_selector_visible("a[href$='/new-tab']")

        rels = self.execute_script("""
            return {
                newTab: document.querySelector("a[href$='/new-tab']").getAttribute("rel"),
                sameTab: document.querySelector("a[href$='/same-tab']").getAttribute("rel"),
            };
            """)
        assert rels == {"newTab": "noopener noreferrer", "sameTab": None}

    @selenium_test
    def test_markdown_page_keeps_katex_math(self):
        page = self.dataset_populator.new_page(
            slug=self._get_random_name(prefix="katex"),
            content_format="markdown",
            content="# Math\n\nThe root is $\\sqrt{x^2}$.",
        )
        self.get(f"published/page?id={page['id']}")
        self.components.pages.markdown_wrapper.wait_for_visible()
        self.wait_for_selector_visible(".katex")

        math = self.execute_script("""
            const katex = document.querySelector(".katex");
            return {
                annotation: katex.querySelector("annotation")?.textContent ?? null,
                svg: katex.querySelector("svg") !== null,
            };
            """)
        assert math == {"annotation": "\\sqrt{x^2}", "svg": True}

    @selenium_test
    def test_markdown_page_keeps_galaxy_help_links(self):
        page = self.dataset_populator.new_page(
            slug=self._get_random_name(prefix="gxhelp"),
            content_format="markdown",
            content="See [the term](gxhelp://unnamed.dataset).",
        )
        self.get(f"published/page?id={page['id']}")
        self.components.pages.markdown_wrapper.wait_for_visible()
        self.wait_for_selector_visible(".markdown-wrapper .text-justify a")

        # useGxUris only rewrites the link if the sanitizer kept the gxhelp: href
        href = self.execute_script("""
            return document.querySelector(".markdown-wrapper .text-justify a").getAttribute("href");
            """)
        assert href.endswith("help/terms/unnamed.dataset")
