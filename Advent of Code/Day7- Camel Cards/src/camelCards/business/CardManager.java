package camelCards.business;

import java.util.ArrayList;
import java.util.Collections;

import camelCards.dataAccess.CardsDao;
import camelCards.entities.abstracts.Hand;

public class CardManager {
	private ArrayList<Hand> hands;
	private CardsDao cardsDao;
	
	public CardManager() {
		cardsDao = new CardsDao();
		hands = cardsDao.getHandsArrayList();
		Collections.sort(hands);
	}
	
	public void showAllCards() {
		calculateTotalPrice();
	}
	
	public int calculateTotalPrice() {
		int totalPrice = 0;
		for(int i=0; i<hands.size(); i++) {
			int rank = i+1;
			Hand hand = hands.get(i);
			totalPrice += hand.getOfferPrice() * rank;
			System.out.printf("%-15s %-10s %-20s %-15s %-20s\n","rank: " + rank+" ->\t" + hand, "->"+( (hand.getjokerHand().toString().equalsIgnoreCase(hand.toString()) ? " - " : hand.getjokerHand())  )," offer price: "+hand.getOfferPrice(), "price: "+hand.getOfferPrice()*rank,hand.getTypeOfHand());
		}
		System.out.println("Total price is "+totalPrice);
		return totalPrice;
	}
}
