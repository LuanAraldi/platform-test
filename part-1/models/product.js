const mongoose = require('mongoose')

const productSchema = mongoose.Schema({
  body: {type: Object, required: true},
  md5: {type: String, required: true},
  created_at : { type : Date, default: Date.now }
})

module.exports = mongoose.model('Product', productSchema)