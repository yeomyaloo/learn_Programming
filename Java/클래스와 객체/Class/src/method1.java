
public class method1 {

		// 필드가 물체의 상태라면, 물체의 행동에 해당하는게 메소드다. 
		//car에 이름과 번호가 있기도 하지만, car는 앞으로 전진할수도 있고 후진하는 행동도 할 수 있다.
		//입력값 : 매개변수(Parameter) 는 어떤 함수를 호출시에 전달되는 값을 의미한다.
		// 인자(Argument)그 전달된 인자를 받아들이는 변수를 의미한다.
		// 결과값 : 리턴값
		
		
		//메소드 선언(클래스가 가지고 있는 기능)/ 클래스 내부에 선언이 된다.
		//public 리턴타입 매소드명 (매개변수 들){ 필요기능 구현 }
		
		//매개변수, 리턴도 없는 형태
		public void method1_1() {
			System.out.println("method1이 실행됩니다.");
		}
		
		//매개변수 1개 리턴값은 없는 형태
		public void method1_2(int x) {
			System.out.println(x + "를 이용한 method2이 실행됩니다.");
		}
		
		//리턴값은 int형으로 있고 매개변수는 없는 형태
		public int method1_3() {
			System.out.println("method3이 실행됩니다..");
			return 10;
		}
		// 리턴값은 없고 매개변수를 x, y로 두 개 받아들인 형태
		public void method1_4(int x, int y) {
			System.out.println(x + y + "를 이용한 method4가 실행됩니다.");
		}
		
		//값을 받아서 값을 출력하는 상태 
		public int method1_5(int y) {
			System.out.println( y + "를 이용한 method5가 실행됩니다.");
			return y*2;
		}
}
