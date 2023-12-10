package camelCards.entities.concretes;

import camelCards.entities.abstracts.Hand;
import camelCards.entities.abstracts.TypeOfHands;

public class ThreeOfAKind extends Hand{
	private char valueOfThree;
	private char first;
	private char second;
	
	public ThreeOfAKind(int offerPrice) {
		super(TypeOfHands.THREE_OF_A_KIND);
		super.setOfferPrice(offerPrice);
	}
	public ThreeOfAKind(ThreeOfAKind threeOfAKind) { // Copy Constructor
		super(threeOfAKind);
		this.valueOfThree = threeOfAKind.getValueOfThree();
		this.first = threeOfAKind.getFirst();
		this.second = threeOfAKind.getSecond();
	}
	
	public char getValueOfThree() {
		return valueOfThree;
	}
	public void setValueOfThree(char valueOfThree) {
		this.valueOfThree = valueOfThree;
	}
	public char getFirst() {
		return first;
	}
	public void setFirst(char first) {
		this.first = first;
	}
	public char getSecond() {
		return second;
	}
	public void setSecond(char second) {
		this.second = second;
	}
	@Override
	public Hand getjokerHand() {
		switch(getNumOfJ()) {
			case 0:
				return new ThreeOfAKind(this);
			case 3:
				FourOfAKind fourOfAKind = new FourOfAKind(getOfferPrice());
				fourOfAKind.setValueOfFour(first);
				fourOfAKind.setFirst(second);
				fourOfAKind.setCardString(getCardString().replaceAll("J", ""+first));
				return fourOfAKind;
			case 1:
				fourOfAKind = new FourOfAKind(getOfferPrice());
				fourOfAKind.setCardString(getCardString().replaceAll("J", ""+valueOfThree));
				fourOfAKind.setValueOfFour(valueOfThree);
				fourOfAKind.setFirst((first == 'J') ? second : first);
				return fourOfAKind;
			default:
				throw new IllegalStateException();
		}
	}
	@Override
	public String toString() {
		return getCardString();
	}
}
