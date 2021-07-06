
public class scope_and_static {
	// 변수는 사용가능한 범위를 갖는다. 이 범위를 변수의 스코프라고 한다
	int globalScope = 10; 
	static int staticVal =7;
	
	public void scopeTest(int value1) {
	//메서드에서 사용될 수 있는 범위
		int localScope1 = 20;
	
		System.out.println(globalScope);
		System.out.println(localScope1);
		System.out.println(value1);
	}
	public void scopeTest2(int value2){
		int localScope2 = 20;
		
		System.out.println(globalScope);
//		System.out.println(localScope1);//사용불가
//		System.out.println(value1);//사용불가
		System.out.println(localScope2);
		System.out.println(value2);
		
	}
	
	
	public static void main(String[] args) {
		//모든 클래스는 인스턴스화 하지 않은 채로 사용할 수 없다. static과 연관되어 있음 
//		System.out.println(globalScope);
//		System.out.println(localScope);
//		System.out.println(value);
		System.out.println(staticVal);
		
		
		//static한 곳에서 static하지 않은 변수를 사용하려면?
		scope_and_static v1 = new scope_and_static();
		System.out.println(v1.globalScope);
		v1.globalScope = 10;
		scope_and_static v2 = new scope_and_static();//scope_and_static은 이 클래스 자체의 이름
		v2.globalScope = 20;
		System.out.println(v1.globalScope);
		System.out.println(v2.globalScope);
		
	}

}
