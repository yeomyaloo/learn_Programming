
public class switch3 {

	public static void main(String[] args) {
		// switch, case, default, break
		
		int value =1;
		
		switch (value) {
			case 1:
				System.out.println("1");
				break;
			case 2:
				System.out.println("2");
				break;
			case 3:
				System.out.println("3");
				break;
			default:
				System.out.println("그 외 다른 숫자");
				}
		String str = "A";
		switch(str) { //이클립스 7버전에서는 문자열도 스위치문에 포함이 가능해졌다.
		
		case "A":
			System.out.println("A");
			break;
		case "B":
			System.out.println("B");
			break;
		}
			
	}

}

