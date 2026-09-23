// Unit tests get a pass-through spy: components can assert what they send to
// the sanitizer and that its result is what ends up in the DOM.
export const sanitizeHtml = jest.fn((html: string | null | undefined) => html ?? "");
