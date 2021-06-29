
public class StringExam {

	public static void main(String[] args) {
		// String은 new라는 연산자가 없어도 인스턴스를 만들어 낼 수 있다. 
		String str1 = "Hello"; //상수영역에 만들어진 hello
		String str2 = "Hello"; // str2는 이미 만들어진 상수영역 hello가 있기 때문에 str1과 같은 인스턴스를 참조한다.
		
		String str3 = new String("Hello"); //상수영역에 있는 것이 아닌 새로 인스턴트를 hip영역에 만들어서 그것을 참조
		String str4 = new String("Hello"); // str3 str4도 마찬가지로 다른 인스턴스를 만들어서 각각 다른 인스턴스를 가르킨다. 
		
		if(str1 == str2) 
			System.out.println("str1 str2는 같은 레퍼런스입니다.");
		if(str3 == str4)
			System.out.println("str3 str4는 같은 레퍼런스입니다.");
		else
			System.out.println("str3 str4는 다른 레퍼런스입니다.");
		
		//한 번 생성된 클래스는 변화하지 않는다. - string의 독특한 점
		
		System.out.println(str1);
		System.out.println(str1.substring(3)); //3번 인덱스만 잘라서 보여주세요
		System.out.println(str1); //한번 만들어진 클래스 값이 변화하지 않는다.!! 	
	}

}
