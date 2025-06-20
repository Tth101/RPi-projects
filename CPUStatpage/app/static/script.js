function populate_tables(memtype, columns, data, j){ 
    out = `   
        <tr>
            <th scope="row" class="text-center">${memtype}</th>
        `

    for(let i = 0; i < columns - 1; i++){
        out += `
            <td class="text-center"> ${data[j]} </td>
        `
        j++
    }

    out += `
        </tr>
    `
    return out
}

function create_table(data){
    data = data.replace(/(?:&#39;)+|[\[\]]+/g, "").split(',') 
    dataindex = 0
    //remove unicode apostrophe and square brackets then split string into array
    var tbody = document.getElementById("table")
    tbody.innerHTML = populate_tables("Memory", 7, data, 0) + populate_tables("Swap", 4, data, 6)
}
window.onload = create_table(data)