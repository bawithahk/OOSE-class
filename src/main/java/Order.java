import java.util.*;

public class Order {

	Admin admin;
	Collection<Product> products;
	Customer customer;
	Payment payment;
	Shipping shipping;
	Collection<Promotion> promotion;
	private int orderID;
	private Date orderDate;
	private String status;
	private double totalAmount;
	private double ShippingFee;

	public double calculateTotal() {
		// TODO - implement Order.calculateTotal
		throw new UnsupportedOperationException();
	}

	/**
	 * 
	 * @param status
	 */
	public void updateStatus(String status) {
		// TODO - implement Order.updateStatus
		throw new UnsupportedOperationException();
	}

	public String generateInvoice() {
		// TODO - implement Order.generateInvoice
		throw new UnsupportedOperationException();
	}

}