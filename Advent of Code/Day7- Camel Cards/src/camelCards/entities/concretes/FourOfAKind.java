package camelCards.entities.concretes;

import camelCards.entities.abstracts.Hand;
import camelCards.entities.abstracts.TypeOfHands;

public class FourOfAKind extends Hand{
	private char valueOfFour;
	private char first;
	
	public FourOfAKind(int offerPrice) {
		super(TypeOfHands.FOUR_OF_A_KIND);
		super.setOfferPrice(offerPrice);
	}
	
	public FourOfAKind(FourOfAKind fourOfAKind) { // Copy Constructor
		super(fourOfAKind);
		this.valueOfFour = fourOfAKind.getValueOfFour();
		this.first = fourOfAKind.getFirst();
	}
	
	public char getValueOfFour() {
		return valueOfFour;
	}
	public void setValueOfFour(char c) {
		this.valueOfFour = c;
	}
	public char getFirst() {
		return first;
	}
	public void setFirst(char c) {
		this.first = c;
	}

	@Override
	public Hand getjokerHand() {
		switch(getNumOfJ()) {
			case 0:
				return new FourOfAKind(this);
			case 1:
				FiveOfAKind fiveOfAKind = new FiveOfAKind(getOfferPrice());
				fiveOfAKind.setValueOfFive(valueOfFour);
				fiveOfAKind.setCardString(getCardString().replaceAll("J", ""+valueOfFour));
				return fiveOfAKind;
			case 4:
				fiveOfAKind = new FiveOfAKind(getOfferPrice());
				fiveOfAKind.setValueOfFive(first);
				fiveOfAKind.setCardString(getCardString().replaceAll("J", ""+first));
				return fiveOfAKind;
			default:
				throw new IllegalStateException();
		}
	}
}
