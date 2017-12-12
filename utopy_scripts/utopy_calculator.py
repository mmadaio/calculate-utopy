__author__ = 'mmadaio'


def csv_to_list(file):  # Converts CSV to list
    output = []
    with open(file, 'rU') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            output.append(row)
    csvfile.close()
    return output



def calculate_utopy():  # Calculates utopy score for each transition probability matrix

    ## Depending on the level of aggregation of your data, these may not be necessary. Our data has Periods, in Sessions, in Dyads.

    dyad_nums = []
    session_nums = []
    period_nums = []

    path = "tpm" ## Relative filepath of folder containing transition probability matrices (TPM)
    filenames = next(os.walk(path))[2]

    for filename in filenames:
        if not filename.endswith(".DS"):
            file = path+"/"+filename
            output = csv_to_list(file)

            new_output = []
            for i in output[1:]:
                item_list = []
                item = i[1:]
                for i in item:
                    i = float(i)
                    item_list.append(i)
                new_output.append(item_list)
            new_output = numpy.array(new_output)

            rows = []


            ## Actual utopy calculation:

            p = len(output)-1

            for r in range(p):
                each_row = []
                for i in range(p):
                    row = i-r
                    each_row.append(row)
                rows.append(each_row)

            dist_to_diag = numpy.array(rows)

            m = dist_to_diag * new_output
            m_plus = sum(sum(numpy.triu(m)))
            m_minus = sum(sum(numpy.tril(m)))

            denom = p * (p-1)
            utopy = 2 * (m_plus - m_minus) / denom



            print "utopy:"
            print utopy
            print file

            # Format output file into each dyad's session's period's utopy scores:

            dyad_num = file[15:17].strip("_")
            session_num = file[17:19].strip("_")
            period_num = file[19:22].strip("_")
            dyad_nums.append(dyad_num)
            session_nums.append(session_num)
            period_nums.append(period_num)
            utopies.append(utopy)


    print dyad_numbers
    print "Dyad_numbers"
    print dyad_nums
    print utopies
    final = zip(dyad_nums, session_nums, period_nums, utopies)
    with open("utopy_final.csv","wb") as result:
            writer= csv.writer( result )

            for row in final:
                print row
                writer.writerow( row )



calculate_utopy()