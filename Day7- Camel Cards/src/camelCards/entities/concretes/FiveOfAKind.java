package camelCards.entities.concretes;

import camelCards.entities.abstracts.Hand;
import camelCards.entities.abstracts.TypeOfHands;

public class FiveOfAKind extends Hand{
	private char valueOfFive;
	
	public FiveOfAKind(int offerPrice) {
		super(TypeOfHands.FIVE_OF_A_KIND);
		super.setOfferPrice(offerPrice);
	}
	public FiveOfAKind(FiveOfAKind fiveOfAKind) { // Copy Constructor
		super(fiveOfAKind);
		this.valueOfFive = fiveOfAKind.getValueOfFive();
	}
	
	public char getValueOfFive() {
		return valueOfFive;
	}
	public void setValueOfFive(char c) {
		this.valueOfFive = c;
	}
	@Override
	public Hand getjokerHand() {
		FiveOfAKind fiveOfAKind = new FiveOfAKind(getOfferPrice());
		fiveOfAKind.setValueOfFive(valueOfFive);
		fiveOfAKind.setCardString(getCardString());
		return fiveOfAKind;
	}
}
