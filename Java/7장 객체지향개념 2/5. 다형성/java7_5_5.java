package javajungsuk;


//부모
class Product{
	int price;//제품가격
	int bonusPoint;//보너스점수
	
	Product(int price){
		this.price = price;
		bonusPoint = (int)(price/10.0); //보너스 점수는 제품 가격의 10%
	}
}


//자손
class Tv extends Product {
	Tv(){
		//조상 클래스의 생성자 Product(int price)를 호출
		super(100); //Tv 가격 100만원으로 설정
	}
	public String toString() {
		return "Tv";
		}
}
class Computer extends Product {
	Computer() {
		super(200);
	}
	public String toString() { 
		return "Computer"; 
		}
}
class Audio extends Product {
	Audio(){ 
		super(50); 
	}
	public String toString() {
		return "Audio";
	}
}


class Buyer { //물건을 사는 사람
	int money = 1000; //소유금액
	int bonusPoint = 0; //보너스점수
	
	void buy(Product p) {
		if (money < p.price) {
			System.out.println("잔액이 부족하여 물건을 살 수 없습니다.");
			return;
		}
		
		money -= p.price;
		bonusPoint += p.bonusPoint;
		System.out.println(p.toString() + "을/를 구입하셨습니다.");
	}
}

class java7_5_5{
	public static void main(String args[]) {
		Buyer b = new Buyer();
		
		b.buy(new Tv());
		b.buy(new Computer());
		
		System.out.println("현재 남은 돈은"+b.money+"만원 입니다.");
		System.out.println("현재 보너스 점수는"+b.bonusPoint+"점입니다.");
	}
	
}
