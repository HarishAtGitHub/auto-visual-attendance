function draw_department_spread(data) {
	var majors_count = {}
	for (i = 0; i < data.length; i++) {
	  person = data[i];
	  if (majors_count[person["majorsFacet"][0]] === undefined) {
	    majors_count[person["majorsFacet"][0]] = 1;
	  } else {
	    majors_count[person["majorsFacet"][0]] = majors_count[person["majorsFacet"][0]] + 1;
	  }
	}
	graph_data = [];
	for (var key in majors_count) {
	  graph_data.push({
	    name: key,
	    y: majors_count[key]
	  });
	}

	Highcharts.chart('department_spread_chart', {
	  chart: {
	    plotBackgroundColor: null,
	    plotBorderWidth: null,
	    plotShadow: false,
	    type: 'pie'
	  },
	  title: {
	    text: 'Distribution of crowd by departments'
	  },
	  tooltip: {
	    pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
	  },
	  plotOptions: {
	    pie: {
	      allowPointSelect: true,
	      cursor: 'pointer',
	      dataLabels: {
		enabled: true,
		format: '<b>{point.name}</b>: {point.percentage:.1f} %',
		style: {
		  color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
		}
	      }
	    }
	  },
	  series: [{
	    name: 'Dept',
	    colorByPoint: true,
	    data: graph_data
	  }]
	});
}

function draw_student_staff(data) {
	var student_staff_count = {}
	for(i = 0; i < data.length; i++ ) { 
	   person = data[i];
	   if (student_staff_count[person["affiliations"].toString()] === undefined) {
	       student_staff_count[person["affiliations"].toString()] = 1;
	   } else {
	       student_staff_count[person["affiliations"].toString()] = student_staff_count[person["affiliations"].toString()] + 1;
	   }
	}
	graph_data = [];
	for(var key in student_staff_count) {
	    graph_data.push({name : key , y :student_staff_count[key]});
	}

	Highcharts.chart('student_staff_chart', {
	    chart: {
		plotBackgroundColor: null,
		plotBorderWidth: null,
		plotShadow: false,
		type: 'pie'
	    },
	    title: {
		text: 'Distribution of crowd by Staff and Student category'
	    },
	    tooltip: {
		pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
	    },
	    plotOptions: {
		pie: {
		    allowPointSelect: true,
		    cursor: 'pointer',
		    dataLabels: {
			enabled: true,
			format: '<b>{point.name}</b>: {point.percentage:.1f} %',
			style: {
			    color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
			}
		    }
		}
	    },
	    series: [{
		name: 'category',
		colorByPoint: true,
		data: graph_data
	    }]
	});
}

function draw_campus_spread(data) {
	var majorCampuses = {}
	for(i = 0; i < data.length; i++ ) { 
	   person = data[i];
	   if (majorCampuses[person["majorCampuses"].toString()] === undefined) {
	       majorCampuses[person["majorCampuses"].toString()] = 1;
	   } else {
	       majorCampuses[person["majorCampuses"].toString()] = majorCampuses[person["majorCampuses"].toString()] + 1;
	   }
	}

	graph_data = [];
	for(var key in majorCampuses) {
	    graph_data.push({name : key , y :majorCampuses[key]});
	}

	Highcharts.chart('campus_spread_chart', {
	    chart: {
		plotBackgroundColor: null,
		plotBorderWidth: null,
		plotShadow: false,
		type: 'pie'
	    },
	    title: {
		text: 'Distribution of crowd by ASU Campus'
	    },
	    tooltip: {
		pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
	    },
	    plotOptions: {
		pie: {
		    allowPointSelect: true,
		    cursor: 'pointer',
		    dataLabels: {
			enabled: true,
			format: '<b>{point.name}</b>: {point.percentage:.1f} %',
			style: {
			    color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
			}
		    }
		}
	    },
	    series: [{
		name: 'Campus',
		colorByPoint: true,
		data: graph_data
	    }]
	});
}
