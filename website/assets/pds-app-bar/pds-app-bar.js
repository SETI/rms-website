(function (window, document, undefined) {
  if (window.PDS_App_Bar !== undefined) {
    return;
  }

  // log proxy function
  var log = function (msg) {
      window.console.log(msg);
    },
    scriptLoader = function (script, func) {
      if (script.onload === undefined) {
        // IE lack of support for script onload
        if (script.onreadystatechange !== undefined) {
          var intervalFunc = function () {
            if (
              script.readyState !== "loaded" &&
              script.readyState !== "complete"
            ) {
              window.setTimeout(intervalFunc, 250);
            } else {
              // it is loaded
              func();
            }
          };
          window.setTimeout(intervalFunc, 250);
        } else {
          log("ERROR: We can't track when script is loaded");
        }
      } else {
        return func;
      }
    };

  window.PDS_App_Bar = function () {
    var app_bar = document.createElement("div"),
      bar_first = document.createElement("div"),
      bar_second = document.createElement("div");
    app_bar.setAttribute("id", "pds-app-bar");
    bar_first.className = "pds-app-bar-section";
    bar_second.className = "pds-app-bar-section";

    var bar_title = document.createElement("a"),
      bar_logo = document.createElement("img");
    bar_title.setAttribute("id", "pds-app-bar-title");
    bar_title.href = "https://pds.nasa.gov/";
    bar_title.target = "_blank";
    bar_title.innerHTML =
      "<img src='https://pds.nasa.gov/pds-app-bar/images/PDS_Planets-acr-inv-bw.png' alt=''>Planetary Data System";
    bar_first.appendChild(bar_title);

    var info_container = document.createElement("div"),
      info_icon = document.createElement("img"),
      info_text = document.createElement("div");
    info_container.setAttribute("id", "pds-app-bar-info");
    info_container.setAttribute("tabindex", "0");
    info_icon.setAttribute("alt", "PDS Information");
    info_icon.setAttribute(
      "src",
      "https://pds.nasa.gov/pds-app-bar/images/info.svg"
    );
    info_text.innerHTML =
      "Find a Node - Use these links to navigate to any of the 8 publicly accessible PDS Nodes." +
      "<br/><br/>" +
      "This bar indicates that you are within the PDS enterprise which includes 6 science discipline nodes and 2 support nodes which are overseen by the Project Management Office at NASA's Goddard Space Flight Center (GSFC). " +
      "Each node is led by an expert in the subject discipline, supported by an advisory group of other practitioners of that discipline, and subject to selection and approval under a regular NASA Research Announcement.";

    info_container.appendChild(info_icon);
    info_container.appendChild(info_text);

    var dropdown_container = document.createElement("div"),
      dropdown_link = document.createElement("a"),
      dropdown_caret = document.createElement("span"),
      dropdown_list = document.createElement("ul");
    dropdown_container.setAttribute("id", "pds-app-bar-dropdown");
    dropdown_link.textContent = "Find a Node";
    dropdown_link.setAttribute("tabindex", "0");
    dropdown_link.appendChild(dropdown_caret);

    var nodes = new Map();
    nodes
      .set("atm", ["Atmospheres (ATM)", "https://pds-atmospheres.nmsu.edu/"])
      .set("img", [
        "Cartography and Imaging Sciences (IMG)",
        "https://pds-imaging.jpl.nasa.gov/",
      ])
      .set("geo", ["Geosciences (GEO)", "https://pds-geosciences.wustl.edu/"])
      .set("naif", [
        "Navigation & Ancillary Information (NAIF)",
        "https://naif.jpl.nasa.gov/naif/",
      ])
      .set("ppi", [
        "Planetary Plasma Interactions (PPI)",
        "https://pds-ppi.igpp.ucla.edu/",
      ])
      .set("rms", ["Ring-Moon Systems (RMS)", "https://pds-rings.seti.org/"])
      .set("sbn", [
        "Small Bodies (SBN)",
        "https://pds-smallbodies.astro.umd.edu/",
      ]);
    for (let value of nodes.values()) {
      let node = document.createElement("a");
      node.textContent = value[0];
      node.href = value[1];
      node.target = "_blank";
      node.setAttribute("tabindex", "-1");
      let li = document.createElement("li");
      li.setAttribute("tabindex", "-1");
      li.appendChild(node);
      dropdown_list.appendChild(li);
    }
    dropdown_container.appendChild(dropdown_link);
    dropdown_container.appendChild(dropdown_list);

    bar_second.appendChild(info_container);
    bar_second.appendChild(dropdown_container);

    app_bar.appendChild(bar_first);
    app_bar.appendChild(bar_second);

    document.body.insertBefore(app_bar, document.body.firstChild);

    var bar_first_style = bar_first.currentStyle || window.getComputedStyle(bar_first);
    info_text.style.left = (bar_first.offsetWidth + parseFloat(bar_first_style.marginRight)).toString() + "px";
    
    dropdown_link.onclick = function () {
      dropdown_container.classList.toggle("active");
    };
    dropdown_link.addEventListener("keydown", (evt) => {
      if (evt.code === "Space" || evt.code === "Enter") {
        dropdown_container.classList.add("active");
        let list_elements = dropdown_list.children,
          list_index = 0;
        list_elements[list_index].setAttribute("tabindex", "0");
        list_elements[list_index].focus();
        dropdown_list.addEventListener("keydown", (e) => {
          if (e.code === "Escape" || e.code === "Tab") {
            list_elements[list_index].setAttribute("tabindex", "-1");
            dropdown_container.classList.remove("active");
            dropdown_link.focus();
          } else if (e.code === "ArrowUp") {
            list_elements[list_index].setAttribute("tabindex", "-1");
            if (list_index === 0) {
              list_index = list_elements.length - 1;
            } else {
              list_index--;
            }
            list_elements[list_index].setAttribute("tabindex", "0");
            list_elements[list_index].focus();
          } else if (e.code === "ArrowDown") {
            list_elements[list_index].setAttribute("tabindex", "-1");
            if (list_index === list_elements.length - 1) {
              list_index = 0;
            } else {
              list_index++;
            }
            list_elements[list_index].setAttribute("tabindex", "0");
            list_elements[list_index].focus();
          } else if (e.code === "Enter") {
            window.open(
              list_elements[list_index].firstElementChild.href,
              "_blank"
            );
          }
        });
      } else if (
        evt.code === "Escape" ||
        (evt.shiftKey && evt.code === "Tab")
      ) {
        dropdown_container.classList.remove("active");
      }
    });

    info_container.onmouseover = function () {
      info_container.classList.add("active");
    };
    info_container.onmouseout = function () {
      info_container.classList.remove("active");
    };
    info_container.onfocus = function () {
      info_container.classList.add("active");
    };
    info_container.onblur = function () {
      info_container.classList.remove("active");
    };
    info_container.addEventListener("keydown", (evt) => {
      if (evt.code === "Escape") {
        info_container.classList.remove("active");
      }
    });

    document.body.onclick = function (e) {
      if (
        e.composedPath && !e.composedPath().some((el) => el.id === "pds-app-bar-dropdown") &&
        dropdown_container.classList.contains("active")
      ) {
        dropdown_container.classList.remove("active");
      }
    };
  };

  // Initialize
  if (document.readyState != "loading") PDS_App_Bar();
  else
    document.addEventListener("DOMContentLoaded", function () {
      PDS_App_Bar();
    });
})(window, document);
