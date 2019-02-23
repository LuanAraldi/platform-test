const Product = require('./../models/product')
const hash = require('object-hash')

const MILLISECONDS_TO_MINUTES_DIVISOR = 60000

function retrieveProductByMD5 (md5) {
  return Product.find({md5: md5})
  .sort({'created_at': -1})
  .limit(1)
  .exec()
}

function parseBody (body) {
  const bodyValueStringified = Object.keys(body)[0]
  try {
    return JSON.parse(bodyValueStringified)
  } catch (e) {
    return new String(bodyValueStringified)
  }
}

function constructor (req) {
  let product = new Product()
  const dados = parseBody(req.body)

  product.body = dados
  product.md5 = hash(dados, {algorithm: 'md5'})

  return product
}

function save(product, response) {
  product.save((err) => {
    if (err) {
      response.status(500).send()
      return true
    } else {
      response.status(200).send()
      return false
    }
  })
}

function minutesInDateDiff(lastProductTimestamp) {
  const dateDiff = Date.now() - lastProductTimestamp
  return Math.floor(dateDiff / MILLISECONDS_TO_MINUTES_DIVISOR);
}

async function newProduct (req, res) {
  let product = this.constructor(req)

  const lastProductAddedWithMD5 = await this.retrieveProductByMD5(product.md5)
  
  if (lastProductAddedWithMD5.length > 0 && this.minutesInDateDiff(lastProductAddedWithMD5[0].created_at) < 10) {
    res.status(403).send()
    return
  }
  console.log(this)
  this.save(product, res)
}

module.exports = {
  constructor: constructor,
  retrieveProductByMD5: retrieveProductByMD5,
  parseBody: parseBody,
  save: save,
  minutesInDateDiff: minutesInDateDiff,
  new: newProduct
}