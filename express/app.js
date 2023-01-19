const http = require('http')

const server = http.createServer((req, res) =>{
    res.writeHeader(200, {'Content-Type': 'text/html'})
    const url = req.url
    if(url === '/'){
        res.write('<h1>Hello World</h1>')
        res.end('Home Page')
    }else if(url === '/about'){
        res.writeHeader(200, {'Content-Type': 'text/html'})
        res.write('<h1>About Page</h1>')
        res.end('About Page')

}else{
    res.writeHeader(404, {'Content-Type': 'text/html'})
    res.write('<h1>404</h1>')
    }
})

server.listen(8000)




