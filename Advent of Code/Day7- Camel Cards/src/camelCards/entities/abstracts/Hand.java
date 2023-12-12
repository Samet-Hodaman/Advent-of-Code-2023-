package camelCards.entities.abstracts;

import camelCards.dataAccess.CardsDao;

public abstract class Hand implements Comparable<Hand>{
	private String cardString;
	private TypeOfHands typeOfHand;
	private int offerPrice;
	
	public Hand(TypeOfHands typeOfHand) {
		this.typeOfHand = typeOfHand;
	}
	public Hand(Hand hand) {
		this.cardString = hand.getCardString();
		this.typeOfHand = hand.getTypeOfHand();
		this.offerPrice = hand.getOfferPrice();
	}
	
	public abstract Hand getjokerHand();
	
	public String getCardString() {
		return cardString;
	}
	public void setCardString(String cardString) {
		this.cardString = cardString;
	}
	
	public int getOfferPrice() {
		return offerPrice;
	}
	public void setOfferPrice(int offerPrice) {
		this.offerPrice = offerPrice;
	}
	public TypeOfHands getTypeOfHand() {
		return typeOfHand;
	}
	public void setTypeOfHand(TypeOfHands typeOfHands) {
		this.typeOfHand = typeOfHands;
	}
	
	protected int getNumOfJ() {
		int numOfJ = 0;
		for(char c : cardString.toCharArray())
			if(c == 'J')
				numOfJ++;
		return numOfJ;
	}
	
	@Override
	public int compareTo(Hand o) {
		int priority = getjokerHand().getTypeOfHand().hasMorePriorityThan(o.getjokerHand().getTypeOfHand());
		if(priority != 0)
			return priority;
		else {
			for(int i=0; i<5; i++) {
				priority = CardsDao.compareCards(cardString.charAt(i), o.getCardString().charAt(i));
				if(priority != 0)
					return priority;
			}
			return 0;
		}
	}
	
	@Override
	public String toString() {
		return cardString;
	}
}