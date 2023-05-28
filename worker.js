addEventListener('fetch', event => {
    event.respondWith(handleRequest(event.request))
  })
  
  async function handleRequest(request) {
    const { pathname } = new URL(request.url)
    const apiKey = '<your-api-key>' 
  
    if (pathname === '/modify-clipboard-link') {
      const data = await request.json()
      const requestApiKey = request.headers.get('X-API-Key')
  
      if (requestApiKey !== apiKey) {
        return new Response(JSON.stringify({ error: 'Invalid API key' }), {
          status: 401,
          headers: { 'Content-Type': 'application/json' },
        })
      }
  
      if ('link' in data) {
        const link = data['link']
        const modifiedLink = link.replace('?forcedownload=1', '?forcedownload=0')
        return new Response(JSON.stringify({ modified_link: modifiedLink }), {
          headers: { 'Content-Type': 'application/json' },
        })
      } else {
        return new Response(JSON.stringify({ error: 'Invalid request' }), {
          status: 400,
          headers: { 'Content-Type': 'application/json' },
        })
      }
    } else {
        const redirectTo = 'https://example.com'; 
        return fetch(redirectTo, request);
      }
  }
  