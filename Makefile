TARGET = mosteller-wallace-federalist-papers.csv
SOURCES = \
  originals/ocr/writings06madiuoft_djvu.txt \
  originals/ocr/writings07madiuoft_djvu.txt
DERIVATIVES = \
  derivatives/federalist.csv \
  derivatives/madison-code315.txt \
  derivatives/madison-money-code302-pp71-80.txt \
  derivatives/madison-neutral-trade-code201-pp204-211.txt \
  derivatives/madison-neutral-trade-code202-pp214-225.txt \
  derivatives/madison-neutral-trade-code203-pp226-235.txt \
  derivatives/madison-neutral-trade-code204-pp235-243.txt \
  derivatives/madison-neutral-trade-code205-pp243-251.txt \
  derivatives/madison-neutral-trade-code206-pp251-259.txt \
  derivatives/madison-neutral-trade-code207-pp259-270.txt \
  derivatives/madison-neutral-trade-code208-pp270-278.txt \
  derivatives/madison-neutral-trade-code209-pp278-285.txt \
  derivatives/madison-neutral-trade-code210-pp285-293.txt \
  derivatives/madison-neutral-trade-code211-pp293-301.txt \
  derivatives/madison-neutral-trade-code212-pp302-310.txt \
  derivatives/madison-neutral-trade-code213-pp310-319.txt \
  derivatives/madison-neutral-trade-code214-pp319-325.txt \
  derivatives/madison-neutral-trade-code215-pp325-334.txt \
  derivatives/madison-neutral-trade-code216-pp334-340.txt \
  derivatives/madison-neutral-trade-code217-pp340-349.txt \
  derivatives/madison-neutral-trade-code218-pp349-357.txt \
  derivatives/madison-neutral-trade-code219-pp357-366.txt \
  derivatives/madison-neutral-trade-code220-pp366-375.txt

all: $(TARGET)

$(TARGET): $(DERIVATIVES)
	python make_dtm.py

$(DERIVATIVES):
	mkdir -p derivatives
	python process_ocr.py
	python process_federalist_csv.py

clean:
	rm -rf derivatives
	rm -f $(TARGET)

.PHONY: all clean
