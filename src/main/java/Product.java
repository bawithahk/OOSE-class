import java.util.*;

public class Product {

	ShoppingCart carts;
	Wishlist wishlist;
	Admin admin;
	Collection<Promotion> promotion;
	Collection<PromotionProduct> promotionProduct;
	Collection<Order> order;
	private int productID;
	private String name;
	private String description;
	private double price;
	private int stockQuantity;
	private String category;

	/**
	 * 
	 * @param quantity
	 */
	public void updateStock(int quantity) {
		// TODO - implement Product.updateStock
		throw new UnsupportedOperationException();
	}

	/**
	 * 
	 * @param discount
	 */
	public void applyDiscount(double discount) {
		// TODO - implement Product.applyDiscount
		throw new UnsupportedOperationException();
	}

}