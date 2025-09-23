# 代码生成时间: 2025-09-23 22:44:59
from bottle import route, run, request, response

# 购物车类，用于管理购物车中的商品
class ShoppingCart:
    def __init__(self):
        self.products = {}

    def add_product(self, product_id, quantity):
        """添加商品到购物车"""
        if product_id in self.products:
            self.products[product_id] += quantity
        else:
            self.products[product_id] = quantity
        return {'message': 'Product added successfully', 'product_id': product_id}

    def remove_product(self, product_id):
        """从购物车中移除商品"""
        if product_id in self.products:
            del self.products[product_id]
            return {'message': 'Product removed successfully', 'product_id': product_id}
        else:
            return {'message': 'Product not found', 'product_id': product_id}

    def get_cart(self):
        """获取购物车中所有商品"""
        return {'products': self.products}

# 创建购物车实例
cart = ShoppingCart()

# API路由
@route('/add_product', method='POST')
def add_product():
    try:
        product_id = request.json['product_id']
        quantity = request.json['quantity']
        response.content_type = 'application/json'
        return cart.add_product(product_id, quantity)
    except KeyError:
        return {'error': 'Missing product_id or quantity in request'}
    except Exception as e:
        return {'error': str(e)}

@route('/remove_product', method='POST')
def remove_product():
    try:
        product_id = request.json['product_id']
        response.content_type = 'application/json'
        return cart.remove_product(product_id)
    except KeyError:
        return {'error': 'Missing product_id in request'}
    except Exception as e:
        return {'error': str(e)}

@route('/get_cart')
def get_cart():
    response.content_type = 'application/json'
    return cart.get_cart()

# 运行服务器
if __name__ == '__main__':
    run(host='localhost', port=8080)