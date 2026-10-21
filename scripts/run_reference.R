# Re-run the 4 R Consortium Pilot 1 TLF programs with current package versions.
pilot <- normalizePath("external/submissions-pilot1")
out_html <- normalizePath("ground_truth/html")
setwd(pilot)  # pilot1wrappers' startup searches upward for DESCRIPTION; must run inside the pilot repo
progs <- c("tlf-demographic", "tlf-primary", "tlf-efficacy", "tlf-kmplot")

results <- data.frame(program = progs, status = NA, message = NA)
for (i in seq_along(progs)) {
  f <- file.path(pilot, "vignettes", paste0(progs[i], ".Rmd"))
  message("\n===== Running ", progs[i], " =====")
  res <- tryCatch({
    rmarkdown::render(f, output_dir = out_html, envir = new.env(), quiet = TRUE)
    "OK"
  }, error = function(e) paste("FAILED:", conditionMessage(e)))
  results$status[i] <- ifelse(res == "OK", "OK", "FAILED")
  results$message[i] <- res
  message(res)
}
print(results[, c("program", "status")])
