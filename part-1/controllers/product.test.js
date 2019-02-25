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
    test('Should have a body property with request body inputs', () => {
      const req = {
        body : { 
          '{"id": "1234", "name": "mesa"}': '' 
        }
      }
      const expectedOutput = {
        body:{
          id: '1234',
          name: 'mesa'
        }
      }
      const constructedProduct = product.constructor(req)
      expect(constructedProduct).toBeDefined()
      expect(constructedProduct).toBeInstanceOf(Object)
      expect(constructedProduct).toMatchObject(expectedOutput)
    })

    test('Should have a md5 property made with request body inputs', () => {
      const req = {
        body : { 
          '{"id": "1234", "name": "mesa"}': '' 
        }
      }
      const expectedOutput = {
        md5: '58e2da437fc12b3ff992d93fd8b7e09d'
      }
      const constructedProduct = product.constructor(req)
      expect(constructedProduct).toBeDefined()
      expect(constructedProduct).toBeInstanceOf(Object)
      expect(constructedProduct).toMatchObject(expectedOutput)
    })
  })

  describe('save method testing', () => {
    test('Use mocked save method to save product', () =>{
      const req = {
        body : { 
          '{"id": "1234", "name": "mesa"}': '' 
        }
      }
      const constructedProduct = product.constructor(req)
      const savedProduct = product.save(constructedProduct)
      expect(savedProduct).toBeDefined()
      expect(savedProduct).toBeTruthy()
    })
  })

  describe('minutesInDateDiff method testing', () => {
    test('Difference beetween two dates need to be 5 minutes', () => {
      const actualDate = new Date(1551044570259)
      const fiveMinutesEarly = new Date(1551044570259 - (60000 * 5))

      const dateDiff = product.minutesInDateDiff(actualDate, fiveMinutesEarly)
      expect(dateDiff).toBeDefined()
      expect(dateDiff).toBe(5)
    })
  })
})