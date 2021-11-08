class Deck{
    final int CARD_NUM = 52;
    Card c[] = new Card[CARD_NUM]

    Deck(){
        int i = 0;
        for (int k = Card.KIND_MAX; k > 0 ; k-- ){
            for(int n = 1; n<Card.NUM_MAX+1;n++){
                c[i++] = new Card(k,n);
            }
        }
    }
    Card pick(int index){
        return c[index%CARD_NUM] //지정된 위치에 있는 카드 하나를 선택한다. 
    }
    Card pick(){
        int index = (int)(Math.random()*CARD_NUM); // 덱에서 카드를 하나 선택한다.
        return pick(index)
    }
    void shuffle() {  // 카드 순서 섞기 
        for(int n = 0l n < 1000; n++){
            int i = (int)(Math.random()*CARD_NUM);
            Card temp = c[0];
            c[0] = c[i]
            c[i] = temp
        }
    }
}