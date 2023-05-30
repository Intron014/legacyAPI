else if(pathname === '/i014-service'){
  const data = await request.json()
  const serviceAPI = 'https://service.intron014.com/api/v1/'
  const serviceAPIrequest = new Request(serviceAPI, request)
  const serviceAPIresponse = await fetch(serviceAPIrequest)
  return serviceAPIresponse
}

else if (host === 'service.intron014.com') {
  // Make a request to another API (example: https://api.example.com)
  const apiUrl = 'https://api.example.com'
  const apiRequest = new Request(apiUrl, request)

  // Set custom parameters
  const params = new URLSearchParams()
  params.append('param1', 'value1')
  params.append('param2', 'value2')
  // Append parameters to the API URL
  const apiUrlWithParams = apiUrl + '?' + params.toString()
  const apiRequest = new Request(apiUrlWithParams, request)
  
  // Set custom headers
  apiRequest.headers.set('Authorization', 'Bearer YOUR_TOKEN')
  apiRequest.headers.set('Content-Type', 'application/json')
  apiRequest.headers.set('X-Custom-Header', 'Custom Value')

  // Make the request to the other API
  const apiResponse = await fetch(apiRequest)

  // Return the response from the other API
  return apiResponse
}