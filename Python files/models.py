from typing import Optional
import datetime
import decimal

from sqlalchemy import Column, DECIMAL, Date, Double, ForeignKeyConstraint, Index, Integer, String, Table
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass


class Admin(Base):
    __tablename__ = 'admin'
    __table_args__ = (
        Index('email', 'email', unique=True),
    )

    adminID: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(50), nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    role: Mapped[str] = mapped_column(String(50), nullable=False)

    product: Mapped[list['Product']] = relationship('Product', back_populates='admin')


class Customer(Base):
    __tablename__ = 'customer'
    __table_args__ = (
        Index('email', 'email', unique=True),
    )

    customerID: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(50), nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    address: Mapped[Optional[str]] = mapped_column(String(400))

    order: Mapped[list['Order']] = relationship('Order', back_populates='customer')
    shoppingcart: Mapped[list['Shoppingcart']] = relationship('Shoppingcart', back_populates='customer')
    wishlist: Mapped[list['Wishlist']] = relationship('Wishlist', back_populates='customer')


class Promotion(Base):
    __tablename__ = 'promotion'
    __table_args__ = (
        Index('Code', 'Code', unique=True),
    )

    PromotionID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Code: Mapped[int] = mapped_column(Integer, nullable=False)
    Description: Mapped[str] = mapped_column(String(400), nullable=False)
    DiscountValue: Mapped[decimal.Decimal] = mapped_column(DECIMAL(10, 2), nullable=False)
    StartDate: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    EndDate: Mapped[datetime.date] = mapped_column(Date, nullable=False)

    order: Mapped[list['Order']] = relationship('Order', back_populates='promotion')
    promotionproduct: Mapped[list['Promotionproduct']] = relationship('Promotionproduct', back_populates='promotion')


class Order(Base):
    __tablename__ = 'order'
    __table_args__ = (
        ForeignKeyConstraint(['PromotionPromotionID'], ['promotion.PromotionID'], name='FKOrder827663'),
        ForeignKeyConstraint(['customerID'], ['customer.customerID'], name='FKOrder872885'),
        Index('FKOrder827663', 'PromotionPromotionID'),
        Index('FKOrder872885', 'customerID')
    )

    orderID: Mapped[int] = mapped_column(Integer, primary_key=True)
    customerID: Mapped[int] = mapped_column(Integer, nullable=False)
    orderDate: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    status: Mapped[str] = mapped_column(String(50), nullable=False)
    totalAmount: Mapped[decimal.Decimal] = mapped_column(Double(asdecimal=True), nullable=False)
    shippingFee: Mapped[decimal.Decimal] = mapped_column(Double(asdecimal=True), nullable=False)
    PromotionPromotionID: Mapped[int] = mapped_column(Integer, nullable=False)

    promotion: Mapped['Promotion'] = relationship('Promotion', back_populates='order')
    customer: Mapped['Customer'] = relationship('Customer', back_populates='order')
    order_items: Mapped[list['OrderItems']] = relationship('OrderItems', back_populates='order')
    payment: Mapped[list['Payment']] = relationship('Payment', back_populates='order')
    shipping: Mapped[list['Shipping']] = relationship('Shipping', back_populates='order')


class Product(Base):
    __tablename__ = 'product'
    __table_args__ = (
        ForeignKeyConstraint(['adminID'], ['admin.adminID'], name='FKProduct987914'),
        Index('FKProduct987914', 'adminID')
    )

    productID: Mapped[int] = mapped_column(Integer, primary_key=True)
    adminID: Mapped[int] = mapped_column(Integer, nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    price: Mapped[decimal.Decimal] = mapped_column(Double(asdecimal=True), nullable=False)
    category: Mapped[str] = mapped_column(String(100), nullable=False)
    stockQuantity: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(400))

    admin: Mapped['Admin'] = relationship('Admin', back_populates='product')
    wishlist: Mapped[list['Wishlist']] = relationship('Wishlist', secondary='wishlist_items', back_populates='product')
    order_items: Mapped[list['OrderItems']] = relationship('OrderItems', back_populates='product')
    promotionproduct: Mapped[list['Promotionproduct']] = relationship('Promotionproduct', back_populates='product')
    shoppingcart_items: Mapped[list['ShoppingcartItems']] = relationship('ShoppingcartItems', back_populates='product')


class Shoppingcart(Base):
    __tablename__ = 'shoppingcart'
    __table_args__ = (
        ForeignKeyConstraint(['customerID'], ['customer.customerID'], name='FKShoppingCa691709'),
        Index('customerID', 'customerID', unique=True)
    )

    cartID: Mapped[int] = mapped_column(Integer, primary_key=True)
    customerID: Mapped[int] = mapped_column(Integer, nullable=False)
    totalAmount: Mapped[decimal.Decimal] = mapped_column(Double(asdecimal=True), nullable=False)
    CustomercustomerID: Mapped[int] = mapped_column(Integer, nullable=False)

    customer: Mapped['Customer'] = relationship('Customer', back_populates='shoppingcart')
    shoppingcart_items: Mapped[list['ShoppingcartItems']] = relationship('ShoppingcartItems', back_populates='shoppingcart')


class Wishlist(Base):
    __tablename__ = 'wishlist'
    __table_args__ = (
        ForeignKeyConstraint(['customerID'], ['customer.customerID'], name='FKWishlist421272'),
        Index('FKWishlist421272', 'customerID')
    )

    wishlistID: Mapped[int] = mapped_column(Integer, primary_key=True)
    customerID: Mapped[int] = mapped_column(Integer, nullable=False)

    customer: Mapped['Customer'] = relationship('Customer', back_populates='wishlist')
    product: Mapped[list['Product']] = relationship('Product', secondary='wishlist_items', back_populates='wishlist')


class OrderItems(Base):
    __tablename__ = 'order_items'
    __table_args__ = (
        ForeignKeyConstraint(['orderID'], ['order.orderID'], name='FKOrder_Item573759'),
        ForeignKeyConstraint(['productID'], ['product.productID'], name='FKOrder_Item111279'),
        Index('FKOrder_Item111279', 'productID')
    )

    orderID: Mapped[int] = mapped_column(Integer, primary_key=True)
    productID: Mapped[int] = mapped_column(Integer, primary_key=True)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    price: Mapped[decimal.Decimal] = mapped_column(Double(asdecimal=True), nullable=False)

    order: Mapped['Order'] = relationship('Order', back_populates='order_items')
    product: Mapped['Product'] = relationship('Product', back_populates='order_items')


class Payment(Base):
    __tablename__ = 'payment'
    __table_args__ = (
        ForeignKeyConstraint(['orderID'], ['order.orderID'], name='FKPayment796685'),
        Index('orderID', 'orderID', unique=True)
    )

    paymentID: Mapped[int] = mapped_column(Integer, primary_key=True)
    orderID: Mapped[int] = mapped_column(Integer, nullable=False)
    amount: Mapped[decimal.Decimal] = mapped_column(Double(asdecimal=True), nullable=False)
    paymentMethod: Mapped[str] = mapped_column(String(100), nullable=False)
    status: Mapped[str] = mapped_column(String(50), nullable=False)
    paymentDate: Mapped[datetime.date] = mapped_column(Date, nullable=False)

    order: Mapped['Order'] = relationship('Order', back_populates='payment')


class Promotionproduct(Base):
    __tablename__ = 'promotionproduct'
    __table_args__ = (
        ForeignKeyConstraint(['ProductID'], ['product.productID'], name='FKPromotionP843406'),
        ForeignKeyConstraint(['PromotionID'], ['promotion.PromotionID'], name='FKPromotionP702748'),
        Index('FKPromotionP702748', 'PromotionID'),
        Index('FKPromotionP843406', 'ProductID')
    )

    PromotionProductID: Mapped[int] = mapped_column(Integer, primary_key=True)
    PromotionID: Mapped[int] = mapped_column(Integer, nullable=False)
    ProductID: Mapped[int] = mapped_column(Integer, nullable=False)

    product: Mapped['Product'] = relationship('Product', back_populates='promotionproduct')
    promotion: Mapped['Promotion'] = relationship('Promotion', back_populates='promotionproduct')


class Shipping(Base):
    __tablename__ = 'shipping'
    __table_args__ = (
        ForeignKeyConstraint(['orderID'], ['order.orderID'], name='FKShipping609903'),
        Index('FKShipping609903', 'orderID')
    )

    shippingID: Mapped[int] = mapped_column(Integer, primary_key=True)
    orderID: Mapped[int] = mapped_column(Integer, nullable=False)
    shippingAddress: Mapped[str] = mapped_column(String(100), nullable=False)
    shippingFee: Mapped[decimal.Decimal] = mapped_column(Double(asdecimal=True), nullable=False)
    shippingStatus: Mapped[str] = mapped_column(String(50), nullable=False)

    order: Mapped['Order'] = relationship('Order', back_populates='shipping')


class ShoppingcartItems(Base):
    __tablename__ = 'shoppingcart_items'
    __table_args__ = (
        ForeignKeyConstraint(['cartID'], ['shoppingcart.cartID'], name='FKShoppingCa711924'),
        ForeignKeyConstraint(['productID'], ['product.productID'], name='FKShoppingCa714936'),
        Index('FKShoppingCa714936', 'productID')
    )

    cartID: Mapped[int] = mapped_column(Integer, primary_key=True)
    productID: Mapped[int] = mapped_column(Integer, primary_key=True)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)

    shoppingcart: Mapped['Shoppingcart'] = relationship('Shoppingcart', back_populates='shoppingcart_items')
    product: Mapped['Product'] = relationship('Product', back_populates='shoppingcart_items')


t_wishlist_items = Table(
    'wishlist_items', Base.metadata,
    Column('WishlistID', Integer, primary_key=True),
    Column('productID', Integer, primary_key=True),
    ForeignKeyConstraint(['WishlistID'], ['wishlist.wishlistID'], name='FKWishlist_I811192'),
    ForeignKeyConstraint(['productID'], ['product.productID'], name='FKWishlist_I792646'),
    Index('FKWishlist_I792646', 'productID')
)
