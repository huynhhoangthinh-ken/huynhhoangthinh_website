import slugMap from './data/slug_map.json';

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const pathname = url.pathname;

    // 1. Handle /article or /article.html with ?id=
    if (pathname === '/article' || pathname === '/article.html') {
      const id = url.searchParams.get('id');
      if (id) {
        if (slugMap[id]) {
          return new Response(null, {
            status: 301,
            headers: {
              'Location': `/article/${slugMap[id]}/`,
              'Cache-Control': 'public, max-age=86400'
            }
          });
        } else {
          return new Response('Không tìm thấy bài viết (Article Not Found)', {
            status: 404,
            headers: { 'Content-Type': 'text/plain; charset=utf-8' }
          });
        }
      }
    }

    // 2. Handle /article/:id or /article/:id/
    const matchId = pathname.match(/^\/article\/(\d+)\/?$/);
    if (matchId) {
      const id = matchId[1];
      if (slugMap[id]) {
        return new Response(null, {
          status: 301,
          headers: {
            'Location': `/article/${slugMap[id]}/`,
            'Cache-Control': 'public, max-age=86400'
          }
        });
      } else {
        return new Response('Không tìm thấy bài viết (Article Not Found)', {
          status: 404,
          headers: { 'Content-Type': 'text/plain; charset=utf-8' }
        });
      }
    }

    return env.ASSETS.fetch(request);
  }
};
