const express = require('express')
const path = require('path')
const app = express()

app.use(express.static(path.join(__dirname, './public')))

// app.get('/', (req, res) => {
//     res.sendFile(path.join(__dirname, './navbar-app/index.html'))
//
// })

app.all('*', (req, res) => {
    res.status(404).send('404 Not Found')
})

app.listen('8000', () => {
    console.log('Server is running on port 8000')
})

