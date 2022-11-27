const nameData = [];
const dateData = [];
const timeData = [];
const detailsData = [];

const fileInput = document.getElementById('uploadfile');
fileInput.onchange = () => {
    //   const selectedFile = fileInput.files[0];
    //   console.log(selectedFile);
    Papa.parse(document.getElementById('uploadfile').files[0],
        {
            download: true,
            header: true,
            skipEmptyLines: true,
            complete: function(results){
                // console.log(results);
                // console.log(results.data[0].name);
                for (i = 0; i < results.data.length; i++) {
                    nameData.push(results.data[i].name)
                    dateData.push(results.data[i].date)
                    timeData.push(results.data[i].time)
                    detailsData.push(results.data[i].details)
                    }

                    eventObj = results.data

                }
            })
        
        }

function fileUpload() { 
    // send file data to python
    return eventObj;
}

// function fileDownload(eventObj) {   
// var csv = Papa.unparse(eventObj);
// }

function fileDownload(csvlist) { 
    var csv = Papa.unparse(csvlist); 
    console.log(csvlist);
    filename = "Events" //add parameter for uploading later 
    var csvFile;  
    var downloadLink;  
     
    //define the file type to text/csv  
    csvFile = new Blob([csv], {type: 'text/csv'});  
    downloadLink = document.createElement("a");  
    downloadLink.download = filename;  
    downloadLink.href = window.URL.createObjectURL(csvFile);  
    downloadLink.style.display = "none";  
  
    document.body.appendChild(downloadLink);  
    downloadLink.click();  
}  

