from flask import Blueprint, jsonify

main_bp = Blueprint('main_bp', __name__)

# Autenticação
main_bp.route('/login', methods = ['POST'])
def login():
    return jsonify({'message':'Realizar login'})

#listagem de produtos
@main_bp.route('/products', methods = ['GET'])
def get_products():
    return jsonify({'message': 'Esta é a rota de listagem de produtos'})


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


