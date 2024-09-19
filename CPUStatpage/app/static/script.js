function populate_tables(memtype, columns, data){ 
    out = `   
        <tr>
            <th scope="row">${memtype}</th>
        `

    for(let i = 0; i > columns - 1; i++){
        out += `
            <td> ${data[i]} </td>
        `
    }

    out += `
        </tr>
    `
    return out
}

function create_table(){
    var tbody = document.getElementById("table")
    tbody.innerHTML = populate_tables("Memory", 6, data) + populate_tables("Swap", 3, data)
}
window.onload = create_table()