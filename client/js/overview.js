var heatmap = h337.create({
  container: document.getElementById("hotmapContainer"),
  radius: 40,
  blur: 0.9,
  maxOpacity: 0.8
});

var positionMap;
$.ajax({
  dataType: "json",
  url: "../positionList.json",
  data: {},
  success: function (data) {
  	positionMap = data;
  },
  async: false
});

var allData;
$.ajax({
  dataType: "json",
  url: "../data.json",
  data: {},
  success: function (data) {
  	allData = data;
  },
  async: false
});

var intervalID = null;

var t = 0;

function freshTime() {
	heatmap.setData({
	  max: 5,
	  data: []
	});

	if (t < 0) {
		t = 0;
		if (intervalID != null)
			clearInterval(intervalID);
		intervalID = null;
	}
	if (t >= allData.length) {
		t = allData.length - 1;
		if (intervalID != null)
			clearInterval(intervalID);
		intervalID = null;
	}

	console.log(t);
	$("#timeInd span").html(t);

	for (i in allData[t]) {
		heatmap.addData({
			x: positionMap[i].ix,
			y: positionMap[i].iy,
			value: allData[t][i]
		})
	}

}

freshTime();
$("#pausebtn").hide();

$("#backbtn").click(function() {
	t-=1;
	freshTime();
})

$("#nextbtn").click(function() {
	t+=1;
	freshTime();
})

$("#playbtn").click(function() {
	$("#playbtn").hide();
	$("#pausebtn").show();
	if (intervalID == null)
		intervalID = setInterval($("#nextbtn").click.bind($("#nextbtn")), 500);
})

$("#pausebtn").click(function() {
	$("#pausebtn").hide();
	$("#playbtn").show();
	if (intervalID != null)
		clearInterval(intervalID);
	intervalID = null;
})
