package camelCards.entities.concretes;

import camelCards.entities.abstracts.Hand;
import camelCards.entities.abstracts.TypeOfHands;

public class FullHouse extends Hand{
	private char valueOfThree;
	private char valueOfTwo;
	
	public FullHouse(int offerPrice) {
		super(TypeOfHands.FULL_HOUSE);
		super.setOfferPrice(offerPrice);
	}
	
	public FullHouse(FullHouse fullHouse) { // Copy Constructor
		super(fullHouse);
		this.valueOfThree = fullHouse.getValueOfThree();
		this.valueOfTwo = fullHouse.getValueOfTwo();
	}
	
	public char getValueOfThree() {
		return valueOfThree;
	}
	public void setValueOfThree(char c) {
		this.valueOfThree = c;
	}
	public char getValueOfTwo() {
		return valueOfTwo;
	}
	public void setValueOfTwo(char c) {
		this.valueOfTwo = c;
	}

	@Override
	public Hand getjokerHand() {
		switch(getNumOfJ()) {
			case 0:
				return new FullHouse(this);
			case 2:
				FiveOfAKind fiveOfAKind = new FiveOfAKind(getOfferPrice());
				fiveOfAKind.setValueOfFive(valueOfThree);
				fiveOfAKind.setCardString(getCardString().replaceAll("J", ""+valueOfThree));
				return fiveOfAKind;
				
			case 3:
				fiveOfAKind = new FiveOfAKind(getOfferPrice());
				fiveOfAKind.setValueOfFive(valueOfTwo);
				fiveOfAKind.setCardString(getCardString().replaceAll("J", ""+valueOfTwo));
				return fiveOfAKind;

			default:
				throw new IllegalStateException();
		}
	}
}
