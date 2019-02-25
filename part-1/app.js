const express = require('express')
const mongoose = require('mongoose')
const bodyparser = require('body-parser')
const app = express()

app.use(bodyparser.json())
app.use(bodyparser.urlencoded({ extended: true }))

mongoose.connect(`mongodb://${process.env.MONGO_IP}:27017/platform`)

const userRoute = require('./routes/product')

app.use(userRoute)

app.listen(3000, () => {
  console.log('Abriu o servidor na porta 3000')
})