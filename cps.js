function fact(n){
	return tail_fact(n,1);
}

function tail_fact(n,a){
	if(n==0)
		return a;
	else
		return tail_fact(n-1, n*a);
}

function fact(n, ret){
	tail_fact(n,1,ret);
}

function tail_fact(n,a,ret){
	if(n==0)
		ret(a);
	else
		tail_fact(n-1,n*a,ret);
}

function fact(n){
	if(n==0)
		return 1;
	else
		return n * fact(n-1);
}

function fact(n,ret){
	if(n==0)
		ret(1);
	else 
		fact(n-1,function (t0){
			ret(n * t0);
		});
}

var num = [3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8];
var ty = [6,6,5,5,5,7,6,6];
var hun =7;
function get_th(){
	var end=0;
	end +=each_hun();
	for(var temp =0; temp<9;++temp){
		end += 100*(num[temp]+10)-3+each_hun();
	}
	console.log(end);
}
function each_hun(){
	var rs=0;
	for (var i in num){
		rs = rs+num[i];
	}
	for(var z =0; z<ty.length;++z){
		rs +=each_ten(ty[z]);
	}
	return rs;
}
function each_ten(ten){
var result =0;
	result += ten;
for (var i =0 ; i<9;i++){

	result += ten+num[i];
}
return result;
}                                                                                                                                                                                                                                                                                                                                                                                                                            ]