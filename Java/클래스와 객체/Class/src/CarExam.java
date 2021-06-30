
public class CarExam {

	public static void main(String[] args) {
		
		//클래스 - 붕어빵 틀
		Car c1 = new Car(); //new라는 연산자 뒤에 나오는 것은 생성자는 메모리에 객체를 만들라는 뜻
		Car c2 = new Car();
		Car c3 = new Car();
		//이렇게 만들어진 만들어진 객체를 참조하는 c1, c2,c3는 참조연산자라고 한다. 
		//car 라는 객체가 3개 만들어진 상태
		
		c1.name = "소방차"; //c1.name은 c1이 참조하는 객체의 네임을 의미 
		c1.number = 1234;
		
		c2.name = "구급차";
		c2.number = 1111;
		
		System.out.println(c1.name);
		System.out.println(c1.number);
		
		System.out.println(c2.name);
		System.out.println(c2.number);
	}

}
