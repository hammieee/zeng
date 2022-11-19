'''
generateDashboard.py will display all saved figures:
1. Ransomware classification learning curve
2. Confusion matrixs
3. Created metrics: accuracy, precision, sensitivity,F1 score, time taken
4. Percentage of ransomware detected in log of interest
'''


def generateDashboard():
    # Creating the HTML file
    file_html = open("index.html", "w")

    # Adding the input data to the HTML file
    file_html.write('''<html>
        <head>
        <style>
        * {
          box-sizing: border-box;
        }

        body {
          margin: 0;
          font-family: Arial;
        }

        /* The grid: Four equal columns that floats next to each other */
        .column {
          float: left;
          width: 16.6%;
          padding: 10px;
        }
        .column2 {
          float: left;
          width: 33.3%;
          padding: 10px;
        }

        /* Style the images inside the grid */
        .column img {
          opacity: 1.0; 
          cursor: pointer; 
        }

        .column img:hover {
          opacity: 1;
        }

        /* Clear floats after the columns */
        .row:after {
          content: "";
          display: table;
          clear: both;
        }

        /* The expanding image container */
        .container {
          position: relative;
          text-align: center;
          display: none;
        }

        /* Expanding image text */
        #imgtext {
          position: absolute;
          bottom: 15px;
          left: 15px;
          color: white;
          font-size: 20px;
        }

        /* Closable button inside the expanded image */
        .closebtn {
          position: absolute;
          top: 10px;
          right: 15px;
          color: white;
          font-size: 35px;
          cursor: pointer;
        }
        </style>
        <title>3204 Dashboard</title>
        </head>
        <body>
        <div style="text-align:center">
          <h2>Ransomware Classification Learning Curve</h2>
        </div>
        <div class="row">
            <div class="column2">
            <img src="images/RandomForest_learning_curve.png" style="width:100%">
          </div>
            <div class="column2">
            <img src="images/NaiveBayes_learning_curve.png" style="width:100%">
          </div>
            <div class="column2">
            <img src="images/SupportVector_learning_curve.png" style="width:100%">
          </div>
          </div>

        </div>

        <br>
        <div style="text-align:center">
          <h2>Confusion Matrix</h2>
        </div>

        <div class="row">
            <div class="column2">
            <img src="images/RandomForest_matrix.png" style="width:100%">
          </div>
            <div class="column2">
            <img src="images/NaiveBayes_matrix.png" style="width:100%">
          </div>
          <div class="column2">
            <img src="images/SupportVector_matrix.png" style="width:100%">
          </div>
        </div>

        <br>
        <div style="text-align:center">
      <h2>Created Metrics</h2>
      <p>Click on the images below:</p>
        </div>

        <!-- The four columns -->
        <div class="row">
          <div class="column">
            <img src="images/0.png" style="width:100%" onclick="myFunction(this);">
          </div>
          <div class="column">
            <img src="images/1.png" style="width:100%" onclick="myFunction(this);" >
          </div>
          <div class="column">
            <img src="images/2.png" style="width:100%" onclick="myFunction(this);" >
          </div>
          <div class="column">
            <img src="images/3.png" style="width:100%" onclick="myFunction(this);" >
          </div>
          <div class="column">
            <img src="images/4.png" style="width:100%" onclick="myFunction(this);">
          </div>
          <div class="column">
            <img src="images/5.png" style="width:100%" onclick="myFunction(this);" >
          </div>
        </div>
        <div class="container">
          <span onclick="this.parentElement.style.display='none'" class="closebtn">&times;</span>
          <img id="expandedImg" style="width:40%">
          <div id="imgtext"></div>
        </div>
        <div style="text-align:center">
          <h2>Percentage of Ransomware detected</h2>
        </div>
        <div class="row" style="text-align:center;">
		  <img src="images/actual.png" style="width:50%">
        </div>
        

        <script>
        function myFunction(imgs) {
          var expandImg = document.getElementById("expandedImg");
          var imgText = document.getElementById("imgtext");
          expandImg.src = imgs.src;
          imgText.innerHTML = imgs.alt;
          expandImg.parentElement.style.display = "block";
        }
        </script>


        </body>
        </html>''')

    # Saving the data into the HTML file
    file_html.close()