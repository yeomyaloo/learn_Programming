
public class StringClass1 {

	public static void main(String[] args) {
		// String클래스가 제공하는 몇가지 메서드를 살펴보자
		
		String str =new String("Hello");
		//일반적으로 뉴라는 함수를 사용해서 객체를 생성해주는 것인데 스트링은 없어도 됨 저 뉴가
		String str2 = "hello World";
		
		System.out.println(str2.length()); //문자열 길이를 구해서 나에게 전해주는 메서드 length
		//공백도 문자로 인식!
		
		System.out.println(str2.concat(" love you!"));
		
		System.out.println(str2);
		//문자열을 붙여도 객체가 참조하는 것이기 때문에 원 str2는 변화하지 않는다!!!
		// string 한번 만들어진 클래스를 바꾸지 않는다. 불변 클래스!! 
		
		
		
		str2 = str2.concat(" love you!");
		System.out.println(str2);
		
		
		//문자 자르기~
		System.out.println(str2.substring(3));
		System.out.println(str2.substring(3, 7));
		
		
	}

}
