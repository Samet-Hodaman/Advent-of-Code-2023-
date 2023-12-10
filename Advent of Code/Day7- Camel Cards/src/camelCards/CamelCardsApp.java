package camelCards;

import camelCards.business.CardManager;

public class CamelCardsApp{
	public static void main(String[] args) {
		CardManager cardManager = new CardManager();
		cardManager.showAllCards();
	}
}