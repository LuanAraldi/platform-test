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
    return bodyValueStringified
  }
}

module.exports = {
  new: async function newProduct (req, res) {
    let product = new Product()
    const dados = parseBody(req.body)

    product.body = dados
    product.md5 = hash(dados, {algorithm: 'md5'})

    const lastProductAddedWithMD5 = await retrieveProductByMD5(product.md5)
    
    if (lastProductAddedWithMD5.length > 0) {
      const dateDiff = Date.now() - lastProductAddedWithMD5[0].created_at
      const minutesInDateDiff = Math.floor(dateDiff / MILLISECONDS_TO_MINUTES_DIVISOR);
      
      if (minutesInDateDiff < 10) {
        res.status(403).send()
        return
      }
    }

    product.save((err) => {
      if (err) {
        res.status(500).send()
      } else {
        res.status(200).send()
      }
    })
  }
}