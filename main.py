from fastapi import FastAPI
import models, schema
from sqlalchemy.orm import Session
from Conexion import SessionLocal, engine
from .models import User, Product, Order, OrderProduct


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def main():
    return RedirectResponse(url="/docs/") #redirrecion tambien pudo habersido a /redoc/ esto para renderizar automaticamente
    
#crear usuario    
@app.post("/users/")
def create_user(user: User, db: Session = Depends(get_db)):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

#mostrar todos los usuarios
@app.get("/users/", response_model=list[User])
def get_all_users(db:Session=Depends(get_db)):
    usuarios = db.query(models.User).all()
    return usuarios

#editar usuario con id
@app.put('/users/{user_id}',response_model=schemas.User)
def update_users(user_id:int,entrada:schemas.UserUpdate,db:Session=Depends(get_db)):
    usuario = db.query(models.User).filter_by(id=user_id).first()
    usuario.nombre=entrada.nombre
    db.commit()
    db.refresh(usuario)
    return usuario

#eliminar usuario
@app.delete('/users/{user_id}',response_model=schemas.Respuesta)
def delete_users(user_id:int,db:Session=Depends(get_db)):
    usuario = db.query(models.User).filter_by(id=user_id).first()
    db.delete(usuario)
    db.commit()
    respuesta = schemas.Respuesta(mensaje="Eliminado exitosamente")
    return respuesta

#crear producto
@app.post("/products/", response_model=Product)
def create_product(product: Product):
    db = SessionLocal()
    producto = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    db.close()
    return producto

#mostrar todos los productos
@app.get("/products/", response_model=list[Product])
def get_all_products(skip: int = 0, limit: int = 10):
    db = SessionLocal()
    products = db.query(models.Product).all()
    db.close()
    return products

#editar producto con id
@app.put('/products/{product_id}',response_model=schemas.User)
def update_users(product_id:int,entrada:schemas.UserUpdate,db:Session=Depends(get_db)):
    producto = db.query(models.User).filter_by(id=product_id).first()
    producto.nombre=entrada.nombre
    db.commit()
    db.refresh(producto)
    return producto

#eliminar producto
@app.delete('/users/{user_id}',response_model=schemas.Respuesta)
def delete_users(user_id:int,db:Session=Depends(get_db)):
    producto = db.query(models.User).filter_by(id=user_id).first()
    db.delete(producto)
    db.commit()
    respuesta = schemas.Respuesta(mensaje="Eliminado exitosamente")
    return respuesta

#obtener todos los productos que ha comprado un usuario
@app.get('/orderproducts/{user_id}',response_model=List[schemas.OrderProduct])
def show_users(db:Session=Depends(get_db)):
    orderproductos = db.query(models.User).all()
    return orderproductos


#obtener todos los productos de un pedido.
@app.get('/usuarios/',response_model=List[schemas.User])
def products_of_orders(db:Session=Depends(get_db)):
    order = db.query(models.Order).filter_by(id=product_id).all()
    return order




