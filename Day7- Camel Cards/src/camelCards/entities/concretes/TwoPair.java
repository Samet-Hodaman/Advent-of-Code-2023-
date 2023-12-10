package camelCards.entities.concretes;

import camelCards.entities.abstracts.Hand;
import camelCards.entities.abstracts.TypeOfHands;

public class TwoPair extends Hand{
	private char valueOfFirstPair;
	private char valueOfSecondPair;
	private char first;
	
	public TwoPair(int offerPrice) {
		super(TypeOfHands.TWO_PAIR);
		super.setOfferPrice(offerPrice);
	}
	public TwoPair(TwoPair twoPair) { // Copy Constructor
		super(twoPair);
		this.valueOfFirstPair = twoPair.getValueOfFirstPair();
		this.valueOfSecondPair = twoPair.getValueOfSecondPair();
		this.first = twoPair.getFirst();
	}
	
	public char getValueOfFirstPair() {
		return valueOfFirstPair;
	}
	public void setValueOfFirstPair(char valueOfFirstPair) {
		this.valueOfFirstPair = valueOfFirstPair;
	}
	public char getValueOfSecondPair() {
		return valueOfSecondPair;
	}
	public void setValueOfSecondPair(char valueOfSecondPair) {
		this.valueOfSecondPair = valueOfSecondPair;
	}
	public char getFirst() {
		return first;
	}
	public void setFirst(char first) {
		this.first = first;
	}
	@Override
	public Hand getjokerHand() {
		switch(getNumOfJ()) {
			case 0:
				return new TwoPair(this);
			case 1:
				FullHouse fullHouse = new FullHouse(getOfferPrice());
				fullHouse.setCardString(getCardString().replaceAll("J", ""+valueOfFirstPair));
				fullHouse.setValueOfThree(valueOfFirstPair);
				fullHouse.setValueOfTwo(valueOfSecondPair);
				return fullHouse;
			case 2:
				FourOfAKind fourOfAKind = new FourOfAKind(getOfferPrice());
				fourOfAKind.setCardString(getCardString().replaceAll("J", (valueOfFirstPair == 'J') ? ""+valueOfSecondPair : ""+valueOfFirstPair));
				fourOfAKind.setValueOfFour((valueOfFirstPair == 'J') ? valueOfSecondPair : valueOfFirstPair);
				fourOfAKind.setFirst(first);
				return fourOfAKind;
			default:
				throw new IllegalStateException();
		}
	}
}
