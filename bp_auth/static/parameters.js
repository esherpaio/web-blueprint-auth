function getParameter(key) {
    let url = new URL(window.location.href);
    return url.searchParams.get(key);
}

function removeParameter(key) {
    let url = new URL(window.location.href);
    url.searchParams.delete(key);
    window.history.replaceState(null, null, url);
}

function getNextPath() {
    const value = getParameter("next");
    if (!value) return null;
    try {
        const url = new URL(value, window.location.origin);
        if (url.origin !== window.location.origin) return null;
        return url.pathname + url.search + url.hash;
    } catch {
        return null;
    }
}
