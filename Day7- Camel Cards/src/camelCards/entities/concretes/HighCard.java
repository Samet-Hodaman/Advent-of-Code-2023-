package camelCards.entities.concretes;

import camelCards.entities.abstracts.Hand;
import camelCards.entities.abstracts.TypeOfHands;

public class HighCard extends Hand{
	private char first;
	private char second;
	private char third;
	private char forth;
	private char fifth;
	
	public HighCard(int offerPrice) {
		super(TypeOfHands.HIGH_CARD);
		super.setOfferPrice(offerPrice);
	}
	public HighCard(HighCard highCard) { // Copy Constructor
		super(highCard);
		this.first = highCard.getFirst();
		this.second = highCard.getSecond();
		this.third = highCard.getThird();
		this.forth = highCard.getForth();
		this.fifth = highCard.getFifth();
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
	public char getThird() {
		return third;
	}
	public void setThird(char third) {
		this.third = third;
	}
	public char getForth() {
		return forth;
	}
	public void setForth(char forth) {
		this.forth = forth;
	}
	public char getFifth() {
		return fifth;
	}
	public void setFifth(char fifth) {
		this.fifth = fifth;
	}
	@Override
	public Hand getjokerHand() {
		switch(getNumOfJ()) {
			case 0:
				return new HighCard(this);
			case 1:
				OnePair onePair = new OnePair(getOfferPrice());
				onePair.setValueOfPair((first == 'J') ? second : first);
				onePair.setFirst((second == 'J') ? third : second);
				onePair.setSecond((third == 'J') ? forth : third);
				onePair.setThird((forth == 'J') ? fifth : forth);
				onePair.setCardString(getCardString().replaceAll("J", ""+onePair.getValueOfPair()));
				return onePair;
			default:
				throw new IllegalStateException();
		}
	}
}