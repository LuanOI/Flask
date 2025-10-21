from flask import Blueprint, jsonify, request
from app import db
from app.models.user import login_pay_load
from pydantic import ValidationError
from bson import objectId

main_bp = Blueprint('main_bp', __name__)

# Autenticação
main_bp.route('/login', methods = ['POST'])
def login():
    try:
        raw_data = request.get_json()
        user_data = login_pay_load(**raw_data)
    except ValidationError as e:
        return jsonify({'error':e.errors}), 400
    except Exception as e:
        jsonify ({'error' : 'Erro durante a requsição do dado'}), 500   
    

    if user_data.username =='admin' and user_data.password =='123':
        return jsonify({'message': 'Login bem-sucedido'})
    else:
        return jsonify({'message': 'credenciais invalidas'})
#listagem de produtos
@main_bp.route('/products', methods = ['GET'])
def get_products():
    products_cursor = db.products.find({})
    products_list = []
    for products in products_cursor:
        products['_id'] = str(products['_id'])
        products_list.append(products)
    return jsonify(products_list)


#Criação de novos produtos
@main_bp.route('/products', methods = ['POST'])
def create_products():
    return jsonify({'message': 'Esta é a rota de criação de produtos'})


#visualização dos detalhes de um unico produto
@main_bp.route('/product/<int:product_id>', methods = ['GET'])
def get_product_by_id(product_id):
    return jsonify({'message': 'Esta é a rota de visualização do detalhe do id do produto{product_id}'})


#atualização de um unico produto e produto existente
@main_bp.route('/product/<int:product_id>', methods = ['PUT'])
def update_product(product_id):
    return jsonify({'message': 'Esta é a rota de atualização do produto com id{product_id}'})

#deleçao de um unico produto e produto existente
@main_bp.route('/product/<int:product_id>', methods = ['DELETE'])
def delete_product(product_id):
    return jsonify({'message': 'Esta é a rota de deleção do produto com id do produto{product_id}'})

# importação de vendas através de um arquivo
@main_bp.route('/sales/upload', methods = ['POST'])
def upload_sales(product_id):
    return jsonify({'message': 'Esta é a rota de upload do arquivo de vendas'})



@main_bp.route('/')
def index():
    return jsonify({'message': 'Bem vindo ao StyleSync'})


