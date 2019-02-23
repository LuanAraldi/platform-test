const product = require('./product')

describe('Product controller test', () => {
  beforeEach(() => {
    product.save = (product) => {
      return true
    }
  })

  describe('parseBody method testing', () => {
    test('Should parse body correctly when its a valid JSON', () => {
      const body = {
        '{"productId":"123", "images":["123.png"]}': ''
      }
  
      const expectedOutput = {
        productId: '123',
        images: ['123.png']
      }
      const parsedBody = product.parseBody(body)
      expect(parsedBody).toBeDefined()
      expect(parsedBody).toEqual(expectedOutput)
      expect(parsedBody).toBeInstanceOf(Object)
    })
  
    test('Should return a string when body is a malformed JSON', () => {
      const body = {
        '{"productId":"123. "images":["123.png"]}': ''
      }
      const parsedBody = product.parseBody(body)
      expect(parsedBody).toBeDefined()
      expect(parsedBody).toBeInstanceOf(String)
    })
  })

  describe('constructor method testing', () => {

  })

  describe('retrieveProductByMD5 method testing', () => {
    
  })

  describe('save method testing', () => {
    
  })

  describe('minutesInDateDiff method testing', () => {
    
  })

  describe('newProduct method testing', () => {
    
  })

})