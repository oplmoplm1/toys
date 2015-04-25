$(function(){
	var ROW = 15;
	var matrix = [];
	function addLine(){
		var rs="";
		rs+="<div class='row'>";
		for(var i=0; i<ROW; i++){
			rs+="<div class='block'></div>";
		}
		rs += "</div>";
		return rs;
	}
	function line(){
		var rs=[];
		for(var i=0; i<ROW; i++){
			rs.push(0);
		}
		return rs;
	}
	function addMatrix(){
		var rs="";
		rs+="<div class='matrix'>";
		for(var i=0; i<ROW; i++){
			rs+=addLine();
			matrix.push(line());
		}
		rs += "</div>";
		return rs;
	}
	$("body").html(addMatrix());
	
	(function(){
		var flag =true;	
		$(document).on("click",".block",function(e){
			if($(this).html()){return;}
			if(flag){
				$(this).html('<div class="black"></div>');
				if(judge.call(this,1)){
					
					flag= true;
					alert("black wins");
					$(document).find(".block").html("");
					return;
				}
				flag=false;
			}else{
				$(this).html('<div class="white"></div>');
				if(judge.call(this,2)){
					
					flag=true;
					alert("white wins");
					$(document).find(".block").html("");
					return;
				}
				flag=true;
			}
		});
		function judge(val){
			var x = $(this).index();
			var y = $(this).parent().index();
			matrix[y][x] = val;
			var xleft = 1,xright=1,v=1,h=1,i,j;
			//xleft
			for(i=x-1,j=y-1;i>=0,j>=0; --j,i--){
				if(matrix[y][x]===matrix[j][i]){
					xleft++;
					if(xleft>=5){
						return true;
					}
				}else{
					break;
				}
			}
			
			for(i=x+1,j=y+1;i<ROW,j<ROW; ++j,i++){
				if(matrix[y][x]===matrix[j][i]){
					xleft++;
					if(xleft>=5){
						return true;
					}
				}else{
					break;
				}
			}
			//xright
			for(i=x-1,j=y+1;i>=0,j<ROW; ++j,i--){
				if(matrix[y][x]===matrix[j][i]){
					xright++;
					if(xright>=5){
						return true;
					}
				}else{
					break;
				}
			}
			for(i=x+1,j=y-1;j>=0,i<ROW; --j,i++){
				if(matrix[y][x]===matrix[j][i]){
					xright++;
					if(xright>=5){
						return true;
					}
				}else{
					break;
				}
			}
			//v 
			for(i=x,j=y+1;j<ROW; ++j){
				if(matrix[y][x]===matrix[j][i]){
					v++;
					if(v>=5){
						return true;
					}
				}else{
					break;
				}
			}
			for(i=x,j=y-1;j>=0; --j){
				if(matrix[y][x]===matrix[j][i]){
					v++;
					if(v>=5){
						return true;
					}
				}else{
					break;
				}
			}
			
		// h
			for(i=x+1,j=y;i<ROW; ++i){
				if(matrix[y][x]===matrix[j][i]){
					h++;
					if(h>=5){
						return true;
					}
				}else{
					break;
				}
			}
			for(i=x-1,j=y;i>=0; --i){
				if(matrix[y][x]===matrix[j][i]){
					h++;
					if(h>=5){
						return true;
					}
				}else{
					break;
				}
			}
			return false;
		}
	})();
});